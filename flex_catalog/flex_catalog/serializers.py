from rest_framework import serializers
from .models import FlexibleCatalogModel

class FlexibleCatalogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlexibleCatalogModel
        fields = ['id', 'name', 'slug',]
