from django.contrib import admin
from .models import Category, Brand, Season, Gender, \
    Color, Size, Product, ProductImage, ProductChildren

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Season)
admin.site.register(Gender)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductChildren)