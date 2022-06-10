from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import NewsletterForm
from .models import Newsletter


def home(request):
    """
    View to render the homepage and
    handle the post request of the NewsletterForm
    """
    if request.method == 'POST':
        newsletterform = NewsletterForm(request.POST)
        emails = Newsletter.objects.all()
        emails = emails.values_list()
        emaillist = [item[1] for item in emails]
        if request.POST['email'] in emaillist:
            messages.info(request, 'You are already subscribed')
        else:
            if newsletterform.is_valid():
                newsletterform.save()
                messages.success(
                    request, 'Thank you for subscribing to our newsletter!'
                )
                return redirect('home')
            else:
                messages.error(
                    request, 'Failed to send. Please check your email address'
                )
    else:
        newsletterform = NewsletterForm()

    template = 'home/index.html'
    context = {
        'newsletterform': newsletterform
    }
    return render(request, template, context)
