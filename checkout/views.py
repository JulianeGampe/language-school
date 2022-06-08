from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderLineItem
from courses.models import Course
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bagcontents
from bag.views import removebag
import stripe
import json


@login_required
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        """
        Reduces the course limit by one
        Prevents booking and removes item from bag
        if the limit is already 0, due to another student booking
        at the same time
        """
        for course_id, course_data in bag.items():
            course = Course.objects.get(id=course_id)
            courselimit = Course.objects.get(id=course_id)
            if courselimit.limit > 0:
                courselimit.limit = courselimit.limit - 1
                courselimit.save()
            else:
                removebag(request, course_id)
                messages.error(
                    request, 'We are sorry, the course is fully booked.'
                )
                return redirect(reverse('viewbag'))

        form_data = {
            'fullname': request.POST['fullname'],
            'email': request.POST['email'],
            'phonenumber': request.POST['phonenumber'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'streetaddress1': request.POST['streetaddress1'],
            'streetaddress2': request.POST['streetaddress2'],
            'county': request.POST['county'],
        }
        orderform = OrderForm(form_data)
        if orderform.is_valid():
            order = orderform.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for course_id, course_data in bag.items():
                try:
                    course = Course.objects.get(id=course_id)
                    if isinstance(course_data, int):
                        orderlineitem = OrderLineItem(
                            order=order,
                            course=course,
                            quantity=course_data,
                        )
                        orderlineitem.save()
                except Course.DoesNotExist:
                    messages.error(
                        request,
                        'One of the courses in your bag \
                            was not found in our database'
                    )
                    order.delete()
                    return redirect(reverse('viewbag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkoutsuccess', args=[order.ordernumber])
            )
        else:
            messages.error(request, 'There was an error with your form.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment"
            )
            return redirect(reverse('allcourses'))

        currentbag = bagcontents(request)
        total = currentbag['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        # Prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                orderform = OrderForm(initial={
                    'email': profile.user.email,
                    'phonenumber': profile.default_phonenumber,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'city': profile.default_city,
                    'streetaddress1': profile.default_streetaddress1,
                    'streetaddress2': profile.default_streetaddress2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                orderform = OrderForm()
        else:
            orderform = OrderForm()

        template = 'checkout/checkout.html'
        context = {
            'orderform': orderform,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


@login_required
def checkoutsuccess(request, ordernumber):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, ordernumber=ordernumber)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.userprofile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phonenumber': order.phonenumber,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_city': order.city,
                'default_streetaddress1': order.streetaddress1,
                'default_streetaddress2': order.streetaddress2,
                'default_county': order.county,
            }
            userprofile_form = UserProfileForm(profile_data, instance=profile)
            if userprofile_form.is_valid():
                userprofile_form.save()

    messages.success(request, 'Thank you, your order is completed')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkoutsuccess.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
