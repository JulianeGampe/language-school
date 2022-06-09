from django.shortcuts import render


def courseinfo(request):
    template = 'courseinfo/courseinfo.html'
    context = {

    }
    return render(request, template, context)
