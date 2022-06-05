from django.shortcuts import render


def profile(request):
    """
    View for the user profile
    """
    template = 'profiles/profiles.html'
    context = {}
    return render(request, template, context)
