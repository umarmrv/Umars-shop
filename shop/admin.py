from django.contrib import admin
from . import models


admin.site.site_header = "Courses Admin"
admin.site.site_title = "Umars Courses"
admin.site.index_title = "Welcome to the Courses area"


class CourseAdmin (admin.ModelAdmin):
    list_display = ('title', 'price', 'category')


class CaregoryAdmin (admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(models.Category, CaregoryAdmin)
admin.site.register(models.Course, CourseAdmin)
