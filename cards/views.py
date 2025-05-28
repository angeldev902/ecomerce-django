from django.shortcuts import render
from rest_framework.views import APIView
from .services.cards_services import CardService
from rest_framework.response import Response
from rest_framework import status

class CardListCreateView(APIView):
    def get(self, request):
        address = CardService.find_all(request.custom_user)
        return Response(address)

    def post(self, request): # Este endpoint solo es para una solución rápida más adelante implementar alguna pasarela de pagos como stripe
        card = CardService.create_card(request.data, request.custom_user)
        return Response({ "message": "Created card" }, status=status.HTTP_201_CREATED)
    
class CardRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        card = CardService.find_one(pk, request.custom_user)
        return Response(card)
    
    def delete(self, request, pk):
        CardService.soft_delete(pk, request.custom_user)
        return Response({ "message": "Deleted card" }, status=status.HTTP_200_OK)