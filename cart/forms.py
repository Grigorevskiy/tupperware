from django import forms
from order.models import Order, OrderInfo
from product.models import Item


class CreateOrder(forms.Form):
    contact_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label=('Contact Phone'))
    delivery_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), label=('Delivery Address'))


    class Meta:
        model = Order
        fields = ('delivery_address', 'contact_phone',)
#
#
# class Additional_order_info(forms.Form):
#     quantity = forms.CharField(widget=forms.TextInput(attrs={'type': 'number', 'length': 50}))
