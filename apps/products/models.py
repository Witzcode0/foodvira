from django.db import models
from apps.master.models import BaseClass


class Category(BaseClass):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Unit(BaseClass):
    name = models.CharField(max_length=200)
    symbol = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.symbol if self.symbol else self.name


class Product(BaseClass):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )

    image = models.ImageField(upload_to="products/main/")
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)

    additional_details = models.JSONField(
        blank=True,
        null=True,
        default=dict
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class ProductImages(BaseClass):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="products/gallery/")

    def __str__(self):
        return f"{self.product.title} Image"
