from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

# TODO: lazy import
from openedx.core.djangoapps.content.course_overviews.serializers import (
    CourseOverviewBaseSerializer,
)

from .models import FlexibleCatalogModel
from .serializers import FlexibleCatalogModelSerializer


# Vista principal para operaciones CRUD
class FlexibleCatalogModelViewSet(ModelViewSet):
    queryset = FlexibleCatalogModel.objects.all()
    serializer_class = FlexibleCatalogModelSerializer

    @action(detail=True, methods=['get'])
    def get_course_runs(self, request, pk=None):
        catalog = self.get_object()
        course_runs = catalog.get_course_runs()
        serializer = CourseOverviewBaseSerializer(course_runs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def search(self, request):
        search_term = request.query_params.get('q', '')
        if not search_term:
            return Response(
                {"detail": "Debe proporcionar un parámetro de búsqueda 'q'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        results = CourseOverview.objects.filter(
            models.Q(title__icontains=search_term) |
            models.Q(description__icontains=search_term)
        )
        serializer = CourseOverviewBaseSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
