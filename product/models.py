from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = ("Category")

    name = models.CharField(max_length=255, verbose_name=('Name'))
    description = models.TextField(verbose_name=('Description'))


    def __str__(self):
        return self.name


class Item(models.Model):
    class Meta:
        verbose_name = ("Item")

    STATUS_CHOICES = (
        (0, ('Not Published')),
        (1, ('Published')),
        (2, ('Sold')),
    )
    sku = models.CharField(max_length=255, verbose_name=('SKU'))
    title = models.CharField(max_length=255, verbose_name=('Name'))
    description = models.TextField(verbose_name=('Description'))
    price = models.IntegerField(verbose_name=('Price'))
    sale_price = models.IntegerField(verbose_name=('Sale Price'), null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name=('Item Count'), default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if not hasattr(self, 'title'):
            return self.title
        return self.title


class ItemPhoto(models.Model):
    item = models.ForeignKey(Item, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item-photos')


class Comment(models.Model):
    item = models.ForeignKey(Item, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=False)
    body = models.TextField(verbose_name=('Comment text'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
