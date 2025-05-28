from django.shortcuts import get_object_or_404
from ..models import Card
from ..serializers import CardSerializer

class CardService:
    @staticmethod
    def find_all(custom_user):
        cards = Card.objects.values('brand', 'last4', 'card_type').filter(deleted=False, user_id=custom_user.id)
        return CardSerializer(cards, many=True).data
    
    @staticmethod
    def create_card(data, custom_user):
        serializer = CardSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=custom_user.id, card_id='Test-KEY-001')
        return serializer.data
    
    @staticmethod
    def find_one(card_id, custom_user):
        card = get_object_or_404(Card, pk=card_id, deleted=False, user_id=custom_user.id)
        return CardSerializer(card).data
    
    @staticmethod
    def soft_delete(card_id, custom_user):
        card = get_object_or_404(Card, pk=card_id, user_id=custom_user.id, deleted=False)
        card.deleted = True
        card.save()