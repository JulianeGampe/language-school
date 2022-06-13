from django.contrib import admin
from .models import Order, OrderLineItem


# Display OrderLineItem on admin site
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitemtotal',)


# Display for Order model on the admin site
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('ordernumber', 'date',
                       'total', 'original_bag',
                       'stripe_pid')

    fields = ('ordernumber', 'userprofile', 'date', 'fullname',
              'email', 'phonenumber', 'country',
              'postcode', 'city', 'streetaddress1',
              'streetaddress2', 'county',
              'total', 'original_bag', 'stripe_pid')

    list_display = ('ordernumber', 'date', 'fullname',
                    'total',)

    ordering = ('-date',)


# Register the order model on the admin site
admin.site.register(Order, OrderAdmin)
