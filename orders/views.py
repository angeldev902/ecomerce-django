from rest_framework.views import APIView
from .services.orders_services import OrdersService
from rest_framework.response import Response
from rest_framework import status

class OrderListCreateView(APIView):
    def get(self, request):
        # params by query
        page = int(request.query_params.get('page', 1))
        limit = int(request.query_params.get('limit', 10))
        
        orders = OrdersService.page(limit, page)
        return Response(orders)

    def post(self, request):
        order = OrdersService.create_order(request.data, request.custom_user)
        return Response({ "message": "Created order" }, status=status.HTTP_201_CREATED)
    
class OrderRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        card = OrdersService.find_one(pk, request.custom_user)
        return Response(card)

class OrderProductDeleteView(APIView):
    def delete(self, request, pk, product_id):
        card = OrdersService.delete_product(request.custom_user, pk, product_id)
        return Response({ "message": "Deleted product from order" }, status=status.HTTP_200_OK)