

def bagcontents(request):
    bagitems = []
    total = 0
    productcount = 0
    context = {
        'bagitems': bagitems,
        'total': total,
        'productcount': productcount
    }
    return context
