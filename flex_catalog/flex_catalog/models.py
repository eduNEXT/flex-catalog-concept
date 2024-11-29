"""
Database models for flex_catalog.
"""
# from django.db import models
from model_utils.models import TimeStampedModel


class FlexibleCatalogModel(TimeStampedModel):
    """
    A flexible model to test replacement options for the discovery service
    """

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        # TODO: return a string appropriate for the data fields
        return '<FlexibleCatalogModel, ID: {}>'.format(self.id)
