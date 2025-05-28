from django.shortcuts import render
from rest_framework.views import APIView
from .services.addresses_service import AddressService
from rest_framework.response import Response
from rest_framework import status

class AddressListCreateView(APIView):
    def get(self, request):
        address = AddressService.find_all(request.custom_user)
        return Response(address)

    def post(self, request):
        address = AddressService.create_address(request.data, request.custom_user)
        return Response({ "message": "Created address" }, status=status.HTTP_201_CREATED)


class AddressRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        address = AddressService.find_one(pk, request.custom_user)
        return Response(address)
    
    def put(self, request, pk):
        category = AddressService.update_address(pk, request.data, request.custom_user)
        return Response({ "message": "Updated address" })
    
    def delete(self, request, pk):
        AddressService.soft_delete(pk, request.custom_user)
        return Response({ "message": "Deleted address" }, status=status.HTTP_200_OK)