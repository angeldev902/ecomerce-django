from django.urls import path, include
from .views import OrderListCreateView, OrderRetrieveUpdateDeleteView, OrderProductDeleteView

urlpatterns = [
    path('', OrderListCreateView.as_view()), # GET /api/orders - POST /api/orders
    path('<int:pk>/', OrderRetrieveUpdateDeleteView.as_view()), # GET /api/orders - POST /api/orders
    path('<int:pk>/product/<int:product_id>/', OrderProductDeleteView.as_view()), # DELETE /api/orders/product - POST /api/orders
]