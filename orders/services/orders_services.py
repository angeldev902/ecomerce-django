from django.shortcuts import get_object_or_404
from ..models import Order, OrderProduct
from datetime import datetime
from django.core.paginator import Paginator
from ..serializers import OrderListSerializer, ProductOrderSerializer, OrderDetailSerializer

class OrdersService:

    @staticmethod
    def generate_order_number():
        """
        Genera un número de orden único con el formato: ORDER-YYYYMMDDHHMMSSffffff
        """
        now = datetime.now()
        return f"ORDER-{now.strftime('%Y%m%d%H%M%S%f')}"
    
    @staticmethod
    def page(limit, page):
        orders = Order.objects.filter(deleted=False).select_related('user').order_by('-created_at')
        paginator = Paginator(orders, limit)
        current_page = paginator.get_page(page)

        serializer = OrderListSerializer(current_page, many=True)

        return {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'current_page': page,
            'results': serializer.data
        }

    @staticmethod
    def create_order(data, custom_user):
        # Valid order
        order = Order.objects.filter(deleted=False, user_id=custom_user.id, status='cart').first()

        if not order:
            order_number = OrdersService.generate_order_number()
            order = Order.objects.create(
                orderNumber=order_number,
                user_id=custom_user.id
            )

        serializer = ProductOrderSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        product_id = serializer.validated_data['product'].id
        product = OrderProduct.objects.filter(order_id=order.id, product_id=product_id).first()
        
        if product:
            serializer = ProductOrderSerializer(product, data=data)
            serializer.is_valid(raise_exception=True)

        serializer.save(order_id=order.id)
        return serializer.data
    
    @staticmethod
    def find_one(order_id, custom_user):
        product = get_object_or_404(Order, pk=order_id, user_id=custom_user.id, deleted=False)
        return OrderDetailSerializer(product).data
    
    @staticmethod
    def delete_product(custom_user, order_id, product_id):
        order = get_object_or_404(Order, pk=order_id, deleted=False, user_id=custom_user.id, status='cart')
        product = get_object_or_404(OrderProduct, pk=product_id, order_id=order_id)
        product.delete()