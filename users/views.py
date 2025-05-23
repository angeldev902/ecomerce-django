from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.user_service import UserService
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action

class UserListCreateView(APIView):
    def get(self, request):
        users = UserService.find_all()
        return Response(users)

    def post(self, request):
        user = UserService.create_user(request.data)
        return Response(user, status=status.HTTP_201_CREATED)

class UserRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk):
        user = UserService.find_one(pk)
        return Response(user)

    def put(self, request, pk):
        user = UserService.update_user(pk, request.data)
        return Response(user)

    def delete(self, request, pk):
        UserService.soft_delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class AuthViewSet(ViewSet):

    @action(detail=False, methods=["post"], url_path="login")
    def post(self, request):
        auth_data = UserService.login(request.data)
        return Response(auth_data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=["post"], url_path="forgot")
    def forgot_password(self, request):
        return Response({"message": "Email enviado para recuperar contraseña"})

    @action(detail=False, methods=["post"], url_path="reset")
    def reset_password(self, request):
        return Response({"message": "Contraseña actualizada"})