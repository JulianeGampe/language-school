from django.shortcuts import render, redirect


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
