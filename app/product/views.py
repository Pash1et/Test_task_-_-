from django.shortcuts import render, get_object_or_404
from .models import Item
import stripe

from django.http import JsonResponse

from django.conf import settings


stripe.api_key = settings.STRIPE_API_KEY_SECRET


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        "item": item,
    }
    return render(request, "product/item_detail.html", context)


def buy_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000/success",
        cancel_url="http://localhost:8000/cancel",
        line_items=[
            {
                "price_data": {
                    "currency": item.currency,
                    "product_data": {
                        "name": item.name,
                    },
                    "unit_amount": int(item.price) * 100,
                },
                "quantity": 1,
            }
        ],
        mode="payment",
    )
    return JsonResponse({"session_id": session.id})


def payment_success(request):
    return render(request, "status/success.html")


def payment_cancel(request):
    return render(request, "status/cancel.html")
