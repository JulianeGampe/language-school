from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .forms import ContactForm


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            contactemail(request, form)
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
        'form': form,
    }
    return render(request, template, context)


"""
Main parts of the following code were taken from Code Institute
def _send_confirmation_email(self, order)
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/250e2c2b8e43cccb56b4721cd8a8bd4de6686546/checkout/webhook_handler.py
"""


def contactemail(request, form):
    """
    Send a confirmation email after submitting the contact form
    """
    cust_email = request.POST['email']
    subject = render_to_string(
        'contact/contact_emails/contact_email_subject.txt',
        {'form': form})
    body = render_to_string(
        'contact/contact_emails/contact_email_body.txt',
        {'form': form, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )
