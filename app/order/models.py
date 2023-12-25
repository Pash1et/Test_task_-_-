from django.db import models
from product.models import Item


class Order(models.Model):
    item = models.ManyToManyField(Item)
    discount = models.ForeignKey(
        "Discount",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )


class Discount(models.Model):
    USD = "USD"
    RUB = "RUB"
    CURENCY_CHOICES = (
        (RUB, "RUB"),
        (USD, "USD"),
    )
    currency = models.CharField(max_length=3, choices=CURENCY_CHOICES)
    percent_off = models.IntegerField()

    def __str__(self) -> str:
        return str(self.percent_off)
