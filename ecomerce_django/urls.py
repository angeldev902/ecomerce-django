from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Django API Rest")


urlpatterns = [
    path('', home),
    path('api/users/', include('users.urls')),
    path('api/brands/', include('brands.urls'))
]
