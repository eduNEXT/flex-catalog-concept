"""
Database models for custom_catalog.
"""

from django.db import models
from model_utils.models import TimeStampedModel
from flex_catalog.models import FlexibleCatalogModel, FixedCatalog

from django.conf import settings


class OdysseyCustomCatalog(FlexibleCatalogModel):
    """
    A catalog that does 1:1 matching (as the fixedcatalog does) but filters the available input courses
    """
    filtered_course_runs = models.ManyToManyField(
        'course_overviews.CourseOverview',
        blank=True,
        related_name='filtered_catalogs',
        limit_choices_to=settings.AVAILABLE_COURSES_FILTER
    )

    def get_course_runs(self):
        """
        Returns the associated course_runs.
        """
        return self.filtered_course_runs.all()

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return '<OdysseyCustomCatalog, ID: {}>'.format(self.id)
