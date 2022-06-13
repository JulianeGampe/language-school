from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course


@login_required
def viewbag(request):
    """
    View to render the shopping bag page
    """
    template = 'bag/bag.html'
    return render(request, template)


@login_required
def addbag(request, course_id):
    """
    Add the chosen course to the bag
    """
    quantity = 1
    redirecturl = request.POST.get('redirecturl')
    bag = request.session.get('bag', {})

    bag[course_id] = quantity

    request.session['bag'] = bag
    messages.success(request, 'The course is in your shopping bag.')
    return redirect(redirecturl)


@login_required
def removebag(request, course_id):
    """
    Remove course from the shopping bag
    """
    course = get_object_or_404(Course, pk=course_id)
    bag = request.session.get('bag', {})
    request.session['bag'] = bag
    if request.method == "POST":
        bag.pop(course_id)
        messages.success(request, 'The course was removed from your bag.')
    return redirect('viewbag')
