from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'ext_number', 'int_number', 'suburb', 'city', 'state', 'country', 'zip_code', 'comments']

    def validate_zip_code(self, value):
        if len(value) != 5:
            raise serializers.ValidationError("Zip code must be exactly 5 characters.")
        if not value.isdigit():
            raise serializers.ValidationError("Zip code must contain only numbers.")
        return value
    
class AddressDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'ext_number', 'int_number', 'suburb', 'city', 'state', 'country', 'zip_code', 'comments']