from django.contrib import admin

from flex_catalog.admin import FixedCatalogAdmin, CourseKeysMixin
from .models import OdysseyCustomCatalog


@admin.register(OdysseyCustomCatalog)
class FixedCatalogAdmin(admin.ModelAdmin, CourseKeysMixin):
    list_display = ('__str__', 'course_keys')
    search_fields = ('flexible_catalog__name', 'flexible_catalog__slug', 'flexible_catalog__id',)
    filter_horizontal = ('filtered_course_runs',)  # Makes managing ManyToMany fields easier in the admin
