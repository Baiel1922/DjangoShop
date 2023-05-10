from django.db import models
from account.models import User
from shop.models import Product, ProductChildren
from account.models import Profile



class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_children = models.ForeignKey(ProductChildren, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

    def add_amount(self, quantity):
        amount = self.product.price * quantity
        profile = Profile.objects.get(user=self.user)
        profile.total_price += amount
        profile.save()
        return True

    def substract_amount(self):
        amount = self.product.price * self.quantity
        profile = Profile.objects.get(user=self.user)
        profile.total_price -= amount
        profile.save()
        return True

