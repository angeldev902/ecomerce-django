from django.db import models
from users.models import User
from addresses.models import Address
from cards.models import Card
from products.models import Product

class OrderProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        related_name='products'
    )

    quantity = models.IntegerField(null=False, blank=False)

    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'order_products'

class Order(models.Model):

    class Status(models.TextChoices):
        CART = 'cart', 'En carrito'
        PENDING_PAYMENT = 'pending_payment', 'Pago pendiente'
        PAID = 'paid', 'Pagado'
        PROCESSING = 'processing', 'Procesando'
        SHIPPED = 'shipped', 'Enviado'
        IN_TRANSIT = 'in_transit', 'En tránsito'
        DELIVERED = 'delivered', 'Entregado'
        CANCELLED = 'cancelled', 'Cancelado'
        RETURNED = 'returned', 'Devuelto'
        REFUNDED = 'refunded', 'Reembolsado'

    class Courier(models.TextChoices):
        DHL = 'dhl', 'DHL'
        ESTAFETA = 'estafeta', 'Estafeta'
        FEDEX = 'fedex', 'Fedex'

    orderNumber = models.CharField(null=False, blank=False, max_length=50, unique=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  
        null=False,               
        blank=False, 
        related_name='orders' # category.products.all() to get all cards in user object   
    )

    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,  
        null=True,               
        blank=True, 
        related_name='orders' 
    )

    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,  
        null=True,               
        blank=True, 
        related_name='orders' 
    )

    courier_name = models.CharField(max_length=10, choices=Courier.choices, null=True, blank=True)

    guide = models.CharField(max_length=20, null=True, blank=True)

    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.CART
    )

    delivery_date = models.DateTimeField(null=True, blank=True)
    
    sended_date = models.DateTimeField(null=True, blank=True)

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'

