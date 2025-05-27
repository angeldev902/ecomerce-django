from rest_framework import serializers
from .models import Category
from utils.strings import slugify

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'parent_category', 'code']

    def create(self, validated_data):
        validated_data['code'] = slugify(validated_data['name'])
        return super().create(validated_data)


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'code']

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'code', 'parent_category', 'created_at', 'updated_at']

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'code']

    def update(self, instance, validated_data):
        name = validated_data.get('name', instance.name)
        instance.name = name
        instance.code = slugify(name)
        instance.save()
        return instance
