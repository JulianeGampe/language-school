from django.contrib import admin
from .models import Newsletter


# Newsletter model display on admin site
class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'email',
    )


# Register the Newsletter model on admin site
admin.site.register(Newsletter, NewsletterAdmin)
