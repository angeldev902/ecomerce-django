import jwt
from django.shortcuts import get_object_or_404
from ..models import Brand
from ..serializers import BrandSerializer, BrandDetailSerializer

class BrandsService:
    @staticmethod
    def find_all():
        brands = Brand.objects.values('id', 'name').filter(deleted=False)
        return BrandDetailSerializer(brands, many=True).data

    @staticmethod
    def create_brand(data):
        serializer = BrandSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def find_one(brand_id):
        brand = get_object_or_404(Brand, pk=brand_id, deleted=False)
        return BrandDetailSerializer(brand).data

    @staticmethod
    def update_brand(brand_id, data):
        brand = get_object_or_404(Brand, pk=brand_id, deleted=False)
        serializer = BrandSerializer(brand, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def soft_delete(brand_id):
        brand = get_object_or_404(Brand, pk=brand_id, deleted=False)
        brand.deleted = True
        brand.save()
