from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course


def viewbag(request):
    """
    View to render the shopping bag page
    """
    template = 'bag/bag.html'
    return render(request, template)


def addbag(request, course_id):
    """
    Add the chosen course to the bag
    """
    quantity = 1
    redirecturl = request.POST.get('redirecturl')
    bag = request.session.get('bag', {})

    bag[course_id] = quantity

    request.session['bag'] = bag
    return redirect(redirecturl)


def removebag(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    bag = request.session.get('bag', {})
    request.session['bag'] = bag
    if request.method == "POST":
        bag.pop(course_id)
    return redirect('viewbag')
