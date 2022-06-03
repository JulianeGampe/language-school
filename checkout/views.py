from django.shortcuts import render, redirect, reverse
from .forms import OrderForm
from django.conf import settings


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('allcourses'))

    orderform = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'orderform': orderform,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
