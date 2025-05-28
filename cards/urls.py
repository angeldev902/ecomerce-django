from django.urls import path, include
from .views import CardListCreateView, CardRetrieveUpdateDeleteView

urlpatterns = [
    path('', CardListCreateView.as_view()), # GET /api/cards - POST /api/cards
    path('<int:pk>/', CardRetrieveUpdateDeleteView.as_view())  # GET /api/cards/:id - PUT - DELETE
]