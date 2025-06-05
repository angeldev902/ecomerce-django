from rest_framework import serializers
from .models import Product, ProductImage
from categories.models import Category
from brands.models import Brand
from utils.strings import slugify

class ProductSerializer(serializers.ModelSerializer):  
    images = serializers.ListField(
        child=serializers.URLField(),
        write_only=True,
        required=True
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'brand', 'images']

    def validate_images(self, value):
        if not value:
            raise serializers.ValidationError("You must provide at least one image.")
        if len(value) > 10:
            raise serializers.ValidationError("You can upload up to 10 images.")
        return value

    def create(self, validated_data):
        validated_data['code'] = slugify(validated_data['name'])
        images_data = validated_data.pop('images')
        product = Product.objects.create(**validated_data)
        for image_url in images_data:
            ProductImage.objects.create(product=product, image_url=image_url)
        return product

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image_url']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']

class ProductListSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'brand', 'images']

class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'code', 'price', 'category', 'brand', 'images']
