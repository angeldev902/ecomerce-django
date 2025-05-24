from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.brands_service import BrandsService
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

class BrandListCreateView(APIView):
    def get(self, request):
        brands = BrandsService.find_all()
        return Response(brands)

    def post(self, request):
        brand = BrandsService.create_brand(request.data)
        return Response({ "message": "Created brand" }, status=status.HTTP_201_CREATED)

class BrandRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        brand = BrandsService.find_one(pk)
        return Response(brand)

    def put(self, request, pk):
        brand = BrandsService.update_brand(pk, request.data)
        return Response({ "message": "Updated brand" })

    def delete(self, request, pk):
        BrandsService.soft_delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
