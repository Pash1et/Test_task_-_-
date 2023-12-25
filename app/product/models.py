from django.db import models


class Item(models.Model):
    USD = "USD"
    RUB = "RUB"
    CURENCY_CHOICES = (
        (RUB, "RUB"),
        (USD, "USD"),
    )
    name = models.CharField(unique=True, max_length=256, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    currency = models.CharField(choices=CURENCY_CHOICES, max_length=3, blank=False)

    def __str__(self) -> str:
        return self.name
