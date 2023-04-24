from django.contrib import admin
from .models import Category, Brand, Season, Gender, Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Season)
admin.site.register(Gender)
admin.site.register(Product)