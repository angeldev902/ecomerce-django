from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings

def home(request):
    return HttpResponse("Django API Rest")


urlpatterns = [
    path('', home),
    path('api/users/', include('users.urls')),
    path('api/brands/', include('brands.urls')),
    path('api/categories/', include('categories.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
