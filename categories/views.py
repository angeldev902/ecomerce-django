from django.shortcuts import render
from rest_framework.views import APIView
from .services.categories_service import CategoriesService
from rest_framework.response import Response
from rest_framework import status

class CategoryListCreateView(APIView):
    def get(self, request):
        brands = CategoriesService.find_all()
        return Response(brands)

    def post(self, request):
        brand = CategoriesService.create_category(request.data)
        return Response({ "message": "Created category" }, status=status.HTTP_201_CREATED)


class CategoryRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        category = CategoriesService.find_one(pk)
        return Response(category)
    
    def put(self, request, pk):
        category = CategoriesService.update_category(pk, request.data)
        return Response({ "message": "Updated category" })
    
    def delete(self, request, pk):
        CategoriesService.soft_delete(pk)
        return Response({ "message": "Deleted category" }, status=status.HTTP_200_OK)