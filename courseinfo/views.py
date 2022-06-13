from django.shortcuts import render


def courseinfo(request):
    """
    Render the courseinfo template
    """
    template = 'courseinfo/courseinfo.html'
    context = {

    }
    return render(request, template, context)
