from django.db import models
from apps.master.models import BaseClass
# Create your models here.

class Category(BaseClass):
    name = models.CharField(max_length=255, null=False, blank=False)
    # slug = models.SlugField()

class Unit(BaseClass):
    name = models.CharField(max_length=200, blank=False, null=False)
    symbol = models.CharField(max_length=15, blank=True, null=True)

class Product(BaseClass):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="")
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField()
    additional_details = models.JSONField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.CharField(max_length=255, default="-")


class ProductImages(BaseClass):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="")

