from django.urls import path

from .views import buy_item, item_detail, payment_cancel, payment_success

urlpatterns = [
    path("item_detail/<int:item_id>/", item_detail, name="item_detail"),
    path("buy_item/<int:item_id>/", buy_item, name="buy_item"),
    path("success", payment_success, name="payment_success"),
    path("cancel", payment_cancel, name="payment_cancel"),
]
