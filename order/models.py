from django.contrib.auth.models import User
from django.db import models
from product.models import Item


class Order(models.Model):
    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")


    ORDER_STATUS_CHOICES = (
        (0, ('New')),
        (1, ('Paid')),
        (2, ('Send to Client')),
    )

    user = models.ForeignKey(User, verbose_name=('Buyer'), on_delete=False)
    items = models.ManyToManyField(Item, related_name='in_orders', through='OrderInfo')
    track_number = models.CharField(max_length=255, verbose_name=('Track Number'), blank=True)
    delivery_address = models.CharField(max_length=255, verbose_name=('Delivery Address'), blank=True)
    contact_phone = models.CharField(max_length=255, verbose_name=('Contact phone'), blank=True)
    status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][0])
    total = models.IntegerField(verbose_name=('Total price'), null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ("Order # ") + str(self.pk)


class OrderInfo(models.Model):
    item_in_order = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count_item = models.IntegerField(default=1)
