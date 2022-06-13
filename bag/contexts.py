from django.shortcuts import get_object_or_404
from courses.models import Course


# Get the items in the shopping bag
def bagcontents(request):
    bagitems = []
    total = 0
    bag = request.session.get('bag', {})

    for course_id, quantity in bag.items():
        course = get_object_or_404(Course, pk=course_id)
        total += quantity * course.price
        bagitems.append({
            'course_id': course_id,
            'quantity': quantity,
            'course': course,
        })

    context = {
        'bagitems': bagitems,
        'total': total,
    }
    return context
