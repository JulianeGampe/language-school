from django.contrib import admin
from .models import Course, Level, Format


# Course model display on admin site
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'level',
        'format',
        'description',
        'price',
        'startdate',
        'weekday',
        'starttime',
        'duration',
        'status',
        'limit',
    )

    ordering = ('name',)


# Level display on admin site
class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'part',
    )


# Format display on admin site
class FormatAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


# Register Course, Level, Format models on admin site
admin.site.register(Course, CourseAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Format, FormatAdmin)
