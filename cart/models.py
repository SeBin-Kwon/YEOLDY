from django.db import models
from products.models import Products
from accounts.models import User

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.cost * self.quantity

    def __str__(self):
        return self.product