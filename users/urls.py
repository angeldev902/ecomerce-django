from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserListCreateView, UserRetrieveUpdateDeleteView, AuthViewSet

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', UserListCreateView.as_view()),          # GET /api/users - POST /api/users
    path('<int:pk>/', UserRetrieveUpdateDeleteView.as_view()),  # GET /api/users/:id - PUT - DELETE
    path('', include(router.urls)),
]
