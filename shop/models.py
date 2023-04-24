from django.db import models

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

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    image = models.ImageField(upload_to='product_images', blank=True)
    price = models.PositiveIntegerField(blank=False)
    currency = models.CharField(max_length=55)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='products')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='products')
    in_stock = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name} {self.price}{self.currency}"