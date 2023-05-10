from django.db import models
from account.models import User
import time

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Category')
    slug = models.CharField(max_length=100, primary_key=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Brand(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Brand')
    slug = models.CharField(max_length=100, primary_key=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Season(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Season')
    slug = models.CharField(max_length=100, primary_key=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Season'
        verbose_name_plural = 'Seasons'


class Gender(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Gender')
    slug = models.CharField(max_length=100, primary_key=True, verbose_name='Slug')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Gender'

class Color(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Color')
    slug = models.CharField(max_length=100, primary_key=True, verbose_name='Slug')
    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Size')
    slug = models.CharField(max_length=100, primary_key=True, verbose_name='Slug')
    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.name

class Product(models.Model):
    zip_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    description = models.TextField()
    main_image = models.ImageField(upload_to='product_images', blank=True)
    price = models.PositiveIntegerField(blank=False)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='products',
        blank=True,
        null=True
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name='products',
        blank=True,
        null=True
    )
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='products')
    # colors = models.ManyToManyField(Color)
    # sizes = models.ManyToManyField(Size)
    is_available = models.BooleanField(default=False)
    # created_at = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name} {self.price}"

class ProductChildren(models.Model):
    product_parent = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_children'
    )
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_children_images', blank=True, null=True)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='product_images')

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
