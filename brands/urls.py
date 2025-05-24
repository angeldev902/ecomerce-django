from django.urls import path, include
from .views import BrandListCreateView, BrandRetrieveUpdateDeleteView

urlpatterns = [
    path('', BrandListCreateView.as_view()),          # GET /api/users - POST /api/users
    path('<int:pk>/', BrandRetrieveUpdateDeleteView.as_view()),  # GET /api/users/:id - PUT - DELETE
]