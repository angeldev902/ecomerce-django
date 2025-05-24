from rest_framework import serializers
from .models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']

class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']