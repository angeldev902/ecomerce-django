from rest_framework.views import APIView
from .services.products_services import ProductsService
from rest_framework.response import Response
from rest_framework import status

class ProductListCreateView(APIView):
    def get(self, request):
        # params by query
        page = int(request.query_params.get('page', 1))
        limit = int(request.query_params.get('limit', 10))
        
        products = ProductsService.page(limit, page)
        return Response(products)

    def post(self, request):
        brand = ProductsService.create_Product(request.data)
        return Response({ "message": "Created product" }, status=status.HTTP_201_CREATED)
    
class ProductRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        product = ProductsService.find_one(pk)
        return Response(product)
        
    def delete(self, request, pk):
        ProductsService.soft_delete(pk)
        return Response({ "message": "Deleted product" }, status=status.HTTP_200_OK)