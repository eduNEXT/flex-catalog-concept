"""
URLs for flex_catalog.
"""
from django.urls import path
from .views import FlexibleCatalogModelViewSet

urlpatterns = [
    path('catalogs/', FlexibleCatalogModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='catalog-list'),
]
