from django.shortcuts import render


def contact(request):
    template = 'contact/contact.html'
    context = {

    }
    return render(request, template, context)
