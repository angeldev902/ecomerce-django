from django.urls import path, include
from .views import ProductListCreateView, ProductRetrieveUpdateDeleteView

urlpatterns = [
    path('', ProductListCreateView.as_view()), # GET /api/products - POST /api/products
    path('<int:pk>/', ProductRetrieveUpdateDeleteView.as_view()),  # GET /api/users/:id - PUT - DELETE
]
