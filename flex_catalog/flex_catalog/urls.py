"""
URLs for flex_catalog.
"""
from django.urls import path
from .views import FlexibleCatalogModelViewSet

urlpatterns = [
    path('catalogs/', FlexibleCatalogModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='catalog-list'),
    path('catalogs/<slug:slug>/course-runs/', FlexibleCatalogModelViewSet.as_view({'get': 'get_course_runs'}), name='catalog-course-runs'),
    path('catalogs/<slug:slug>/search/', FlexibleCatalogModelViewSet.as_view({'get': 'get_search'}), name='catalog-search'),
]
