from django.shortcuts import get_object_or_404
from ..models import Category
from ..serializers import CategorySerializer, CategoryDetailSerializer, CategoryListSerializer, CategoryUpdateSerializer
from rest_framework.exceptions import NotFound, ValidationError

class CategoriesService:
    @staticmethod
    def find_all():
        categories = Category.objects.values('id', 'name', 'code').filter(deleted=False)
        return CategoryListSerializer(categories, many=True).data

    @staticmethod
    def create_category(data):
        serializer = CategorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        parent = serializer.validated_data.get('parent_category')

        if Category.objects.filter(name=name).exists():
            raise ValidationError({'error': 'There is already a category with that name'})
        
        if parent and parent.deleted:
            raise NotFound({'error': 'Parent category is deleted'})
        
        serializer.save()
        return serializer.data

    @staticmethod
    def find_one(category_id):
        category = get_object_or_404(Category, pk=category_id, deleted=False)
        return CategoryDetailSerializer(category).data
    
    @staticmethod
    def update_category(category_id, data):
        category = get_object_or_404(Category, pk=category_id, deleted=False)
        serializer = CategoryUpdateSerializer(category, data=data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']

        if Category.objects.filter(name=name).exists():
            raise ValidationError({'error': 'There is already a category with that name'})
        
        serializer.save()
        return serializer.data
        

    
    @staticmethod
    def soft_delete(category_id):
        category = get_object_or_404(Category, pk=category_id, deleted=False)
        category.deleted = True
        category.save()