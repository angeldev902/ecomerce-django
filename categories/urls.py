from django.urls import path, include
from .views import CategoryListCreateView, CategoryRetrieveUpdateDeleteView

urlpatterns = [
    path('', CategoryListCreateView.as_view()), # GET /api/categories - POST /api/categories
    path('<int:pk>/', CategoryRetrieveUpdateDeleteView.as_view()),  # GET /api/users/:id - PUT - DELETE
]