from django.db import models
from django.contrib.auth.models import User
from product.models import Item


class Wishlist(models.Model):
    user = models.OneToOneField(User, related_name='wishlist', on_delete=models.CASCADE)
    item = models.ManyToManyField(Item)
