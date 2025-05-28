from django.urls import path, include
from .views import AddressListCreateView, AddressRetrieveUpdateDeleteView

urlpatterns = [
    path('', AddressListCreateView.as_view()), # GET /api/address - POST /api/address
    path('<int:pk>/', AddressRetrieveUpdateDeleteView.as_view())  # GET /api/address/:id - PUT - DELETE
]