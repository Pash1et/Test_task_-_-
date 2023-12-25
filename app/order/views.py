import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Order

stripe.api_key = settings.STRIPE_API_KEY_SECRET


def buy_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    line_items = []
    coupon = None
    if order.discount:
        coupon = stripe.Coupon.create(
            percent_off=order.discount.percent_off,
            duration="once",
        )
    for item in order.item.all():
        line_items.append(
            {
                "price_data": {
                    "currency": "RUB",
                    "product_data": {
                        "name": item.name,
                    },
                    "unit_amount": int(item.price) * 100,
                },
                "quantity": 1,
            }
        )
    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000/success",
        cancel_url="http://localhost:8000/cancel",
        line_items=line_items,
        mode="payment",
        discounts=[{"coupon": coupon} if coupon else {"coupon": None}],
        automatic_tax={"enabled": True},
    )
    return JsonResponse({"session_id": session.id})


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    context = {
        "order": order,
    }
    return render(request, "order/order_detail.html", context)
