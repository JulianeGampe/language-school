from django.shortcuts import get_object_or_404
from courses.models import Course


def bagcontents(request):
    bagitems = []
    total = 0
    productcount = 0
    bag = request.session.get('bag', {})

    for course_id, quantity in bag.items():
        course = get_object_or_404(Course, pk=course_id)
        total = quantity * course.price
        productcount = quantity
        bagitems.append({
            'course_id': course_id,
            'quantity': quantity,
            'course': course,
        })

    context = {
        'bagitems': bagitems,
        'total': total,
        'productcount': productcount,
    }
    return context
