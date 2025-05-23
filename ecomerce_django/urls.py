from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hola, esta es la raíz del proyecto")


urlpatterns = [
    path('', home),
    path('api/users/', include('users.urls'))
]
