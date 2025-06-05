from django.db import models
from categories.models import Category
from brands.models import Brand

class ProductImage(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image_url = models.URLField(null=False, blank=False, max_length=500)

    class Meta:
        db_table = 'product_images'

class Product(models.Model):

    name = models.CharField(null=False, blank=False, max_length=30, unique=True)

    code = models.CharField(null=False, blank=False, max_length=30, unique=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, null=False) # Esta bien este tipo para guardar valores numericos

    description = models.TextField(null=False, blank=False) # La descripción sera tan larga como quiero

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  
        null=False,               
        blank=False, 
        related_name='products' # category.products.all() to get all cards in user object   
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,  
        null=False,               
        blank=False, 
        related_name='products' # brand.products.all() to get all cards in user object   
    )

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'