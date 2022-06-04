from django.shortcuts import render, redirect, reverse
from django.conf import settings
from .forms import OrderForm
from bag.contexts import bagcontents
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('allcourses'))

    currentbag = bagcontents(request)
    total = currentbag['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )

    print(intent)

    orderform = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'orderform': orderform,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
