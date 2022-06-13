from django.contrib import admin
from .models import Contact


# Contact model display on admin site
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phonenumber',
        'message',
        'reason',
    )


# Register the Contact model on the admin site
admin.site.register(Contact, ContactAdmin)
