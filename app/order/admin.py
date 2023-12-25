from django.contrib import admin

from .models import Discount, Order


@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "discount")


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("id", "currency", "percent_off")
