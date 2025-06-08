import jwt
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed
from ..models import User
from ..serializers import UserSerializer, LoginSerializer
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

class UserService:
    @staticmethod
    def find_all():
        users = User.objects.filter(deleted=False)
        return UserSerializer(users, many=True).data

    @staticmethod
    def create_user(data):
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def find_one(user_id):
        user = get_object_or_404(User, pk=user_id, deleted=False)
        return UserSerializer(user).data

    @staticmethod
    def update_user(user_id, data):
        user = get_object_or_404(User, pk=user_id, deleted=False)
        serializer = UserSerializer(user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def soft_delete(user_id):
        user = get_object_or_404(User, pk=user_id, deleted=False)
        user.deleted = True
        user.save()

    @staticmethod
    def login(data):
        serializer = LoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = get_object_or_404(User, email=email, deleted=False)

        try:
            user = User.objects.get(email=email, deleted=False)
        except User.DoesNotExist:
            raise AuthenticationFailed("User not fount.")

        if not check_password(password, user.password):
            raise AuthenticationFailed("Incorrect Password")
        else:
            payload = {
                "user_id": user.id,
                "exp": datetime.now() + timedelta(hours=1),
                "iat": datetime.now()
            }

            token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
            return { "accessToken": token }
        
    @staticmethod
    def get_user_from_token(payload):
            try:
                return User.objects.get(pk=payload['user_id'])
            except ObjectDoesNotExist:
                return None


        
