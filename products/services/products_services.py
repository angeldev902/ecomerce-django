from django.shortcuts import get_object_or_404
from ..models import Product, ProductImage
from ..serializers import ProductSerializer, ProductListSerializer, ProductDetailSerializer
from rest_framework.exceptions import NotFound, ValidationError
from django.core.paginator import Paginator

class ProductsService:
    @staticmethod
    def find_all():
        products = Product.objects.values('name', 'price', 'description').filter(deleted=False)
        return ProductListSerializer(products, many=True).data
    
    @staticmethod
    def page(limit, page):
        # products = Product.objects.filter(deleted=False).order_by('-created_at')
        # products = Product.objects.filter(deleted=False).only('id', 'name', 'price', 'category_id', 'brand_id').prefetch_related('images').order_by('-created_at')
        products = Product.objects.filter(deleted=False).select_related('category', 'brand').prefetch_related('images').order_by('-created_at')
        paginator = Paginator(products, limit)
        current_page = paginator.get_page(page)

        serializer = ProductListSerializer(current_page, many=True)

        return {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'current_page': page,
            'results': serializer.data
        }

    @staticmethod
    def create_Product(data):
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        category = serializer.validated_data.get('category')
        brand = serializer.validated_data.get('brand')

        if Product.objects.filter(name=name).exists():
            raise ValidationError({'error': 'There is already a product with that name'})
        
        if category and category.deleted:
            raise NotFound({'error': 'Category is deleted'})
        
        if brand and brand.deleted:
            raise NotFound({'error': 'Brand is deleted'})
        
        serializer.save()
        return serializer.data
    
    @staticmethod
    def find_one(product_id):
        product = get_object_or_404(Product, pk=product_id, deleted=False)
        return ProductDetailSerializer(product).data
    

    @staticmethod
    def soft_delete(product_id):
        product = get_object_or_404(Product, pk=product_id, deleted=False)
        product.deleted = True
        product.save()