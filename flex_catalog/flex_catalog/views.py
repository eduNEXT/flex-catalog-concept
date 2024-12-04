from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from openedx.core.djangoapps.content.course_overviews.serializers import (
    CourseOverviewBaseSerializer,
)

from .models import FlexibleCatalogModel
from .serializers import FlexibleCatalogModelSerializer


class FlexibleCatalogModelViewSet(ModelViewSet):
    queryset = FlexibleCatalogModel.objects.all()
    serializer_class = FlexibleCatalogModelSerializer

    def get_queryset(self):
        """
        Overrides the queryset to fetch subclass instances.
        """
        return FlexibleCatalogModel.objects.select_related().select_subclasses()

    def get_object(self):
        """
        Ensures the retrieved object is the specific subclass.
        Note: Not entirely sure this is needed after select_subclasses
        """
        obj = super().get_object()
        # Cast to the correct subclass if not already resolved
        if hasattr(obj, 'cast'):
            return obj.cast()
        return obj

    @action(detail=True, methods=['get'])
    def get_course_runs(self, request, pk=None):
        """
        Forward the REST view to the get_course_runs in the object.
        """
        course_runs = self.get_object().get_course_runs()
        serializer = CourseOverviewBaseSerializer(course_runs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Forward the REST view to the get_course_runs in the object.
        """
        search_term = request.query_params.get('q', '')
        if not search_term:
            return Response(
                {"detail": "Must pass a search query 'q'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        results = self.get_object().get_course_runs().filter(
            models.Q(title__icontains=search_term) |
            models.Q(description__icontains=search_term)
        )
        serializer = CourseOverviewBaseSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
