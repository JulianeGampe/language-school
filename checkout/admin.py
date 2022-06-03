from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitemtotal',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('ordernumber', 'date',
                       'total',)

    fields = ('ordernumber', 'date', 'fullname',
              'email', 'phonenumber', 'country',
              'postcode', 'city', 'streetaddress1',
              'streetaddress2', 'county',
              'total',)

    list_display = ('ordernumber', 'date', 'fullname',
                    'total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
