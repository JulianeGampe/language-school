from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    """
    View for the user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }
    return render(request, template, context)


def orderhistory(request, ordernumber):
    order = get_object_or_404(Order, ordernumber=ordernumber)

    template = 'checkout/checkoutsuccess.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
