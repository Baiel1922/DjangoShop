from django.contrib import admin
from .models import Category, Brand, Season, Gender, \
    Color, Size, Product, ProductImage, ProductChildren, ProductChildrenImage


class ProductChildrenInline(admin.TabularInline):
    model = ProductChildren
    fields = ()
    extra = 3


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ()
    extra = 3

class ProductChildrenImageInline(admin.TabularInline):
    model = ProductChildrenImage
    fields = ()
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category', 'is_available')
    list_display_link = ('pk', 'name', 'category', 'is_available')
    list_filter = ('category', 'brand', 'season', 'gender', 'is_available', 'price')
    search_fields = ('name', 'zip_code', 'description')
    inlines = [
        ProductChildrenInline,
        ProductImageInline
    ]
class ProductChildrenAdmin(admin.ModelAdmin):
    list_display = ('pk', 'color', 'size', 'is_available')
    list_display_link = ('pk', 'color', 'size', 'is_available')
    list_filter = ('color', 'size', 'quantity', 'is_available')
    search_fields = ('pk', )
    inlines = [
        ProductChildrenImageInline,
    ]
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_link = ('name', 'slug')
    search_fields = ('name', 'slug')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_link = ('name', 'slug')
    search_fields = ('name', 'slug')


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_link = ('name', 'slug')
    search_fields = ('name', 'slug')


class GenderAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_link = ('name', 'slug')
    search_fields = ('name', 'slug')


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_link = ('name', 'slug')
    search_fields = ('name', 'slug')

class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_link = ('name', 'slug')
    search_fields = ('name', 'slug')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Season, SizeAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductChildren, ProductChildrenAdmin)