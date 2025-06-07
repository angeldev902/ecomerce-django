from rest_framework import serializers
from .models import Order, OrderProduct
from users.models import User
from addresses.models import Address
from cards.models import Card
from products.models import Product

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['display_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'ext_number', 'int_number', 'suburb', 'city', 'state', 'country', 'zip_code', 'comments']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['brand', 'last4', 'card_type']

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']  # Solo los campos del producto que quieres mostrar

class OrderProductSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer(read_only=True)

    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity', 'amount']  # Solo los que necesitas

class OrderListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'orderNumber', 'status', 'created_at', 'user']

class OrderDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    card = CardSerializer(read_only=True)
    products = OrderProductSerializer(many=True, read_only=True)  # related_name='products' en OrderProduct.order

    class Meta:
        model = Order
        fields = ['id', 'orderNumber', 'status', 'created_at', 'user', 'address', 'card', 'courier_name', 'guide', 'total', 'sended_date', 'delivery_date', 'created_at', 'products']