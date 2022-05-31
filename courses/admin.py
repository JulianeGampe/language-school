from django.contrib import admin
from .models import Course, Level, Format


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
    )

    ordering = ('name',)


class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'friendlyname',
        'name',
    )


class FormatAdmin(admin.ModelAdmin):
    list_display = (
        'friendlyname',
        'name',
    )


admin.site.register(Course, CourseAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Format, FormatAdmin)
