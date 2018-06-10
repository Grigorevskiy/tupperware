from django.contrib.auth.models import User
from product.models import Item
from django.db import models
from django.core.validators import MinValueValidator


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through='CartInfo')
    last_change = models.DateTimeField(auto_now_add=True)


class CartInfo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    count_item = models.PositiveIntegerField(validators=[MinValueValidator(1)])
