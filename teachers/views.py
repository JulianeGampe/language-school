from django.shortcuts import render


def teachers(request):
    """
    View to render the teachers page
    """
    template = 'teachers/teachers.html'
    context = {

    }
    return render(request, template, context)
