from django.shortcuts import render, redirect, reverse
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('allcourses'))

    orderform = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'orderform': orderform
    }

    return render(request, template, context)
