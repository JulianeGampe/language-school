from django.shortcuts import render


def viewbag(request):
    """
    View to render the shopping bag page
    """
    template = 'bag/bag.html'
    return render(request, template)
