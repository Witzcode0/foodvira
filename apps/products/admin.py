from django.contrib import admin
from apps.products.models import Category, Unit, Product, ProductImages
# Register your models here.

admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Product)
admin.site.register(ProductImages)