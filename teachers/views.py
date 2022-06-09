from django.shortcuts import render


def teachers(request):
    template = 'teachers/teachers.html'
    context = {

    }
    return render(request, template, context)
