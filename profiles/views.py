from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """
    View for the user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please check the form.')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, template, context)


@login_required
def orderhistory(request, ordernumber):
    """
    Display order history confirmation
    """
    order = get_object_or_404(Order, ordernumber=ordernumber)

    messages.info(
        request, 'This is a past confirmation. \
            A confirmation email was sent on the order date.'
    )

    template = 'checkout/checkoutsuccess.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
