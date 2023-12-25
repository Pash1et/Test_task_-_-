from django.urls import path

from .views import buy_order, order_detail

urlpatterns = [
    path("buy_order/<int:order_id>/", buy_order, name="buy_order"),
    path("order_detail/<int:order_id>/", order_detail, name="order_detail"),
]
