from django.shortcuts import get_object_or_404
from ..models import Address
from ..serializers import AddressSerializer, AddressDetailSerializer

class AddressService:
    @staticmethod
    def find_all(custom_user):
        addresses = Address.objects.values('id', 'street', 'ext_number', 'int_number', 'suburb', 'city', 'state', 'country', 'zip_code', 'comments').filter(deleted=False, user_id=custom_user.id)
        return AddressDetailSerializer(addresses, many=True).data
    
    @staticmethod
    def create_address(data, custom_user):
        serializer = AddressSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=custom_user.id)
        return serializer.data

    @staticmethod
    def find_one(address_id):
        address = get_object_or_404(Address, pk=address_id, deleted=False)
        return AddressDetailSerializer(address).data

    @staticmethod
    def update_address(address_id, data):
        category = get_object_or_404(Address, pk=address_id, deleted=False)
        serializer = AddressSerializer(category, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
    

    @staticmethod
    def soft_delete(address_id):
        address = get_object_or_404(Address, pk=address_id, deleted=False)
        address.deleted = True
        address.save()