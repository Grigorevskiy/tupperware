from django.contrib.auth.models import User
from product.models import Item
from django.db import models


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)
    last_change = models.DateTimeField(auto_now_add=True)
