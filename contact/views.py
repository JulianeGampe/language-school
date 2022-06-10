from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact form submitted')
            return redirect('home')
        else:
            messages.error(
                request, 'Failed to send. Please check the form'
            )
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form
    }
    return render(request, template, context)
