from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartInfo
from product.models import Item
from order.forms import CreateOrder
from order.models import Order, OrderInfo


def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user_id=request.user.id)

        # calculate total for price in cart items
        cart_total = 0
        for i in cart.cartinfo_set.all():
            if i.item.sale_price:
                cart_total += (i.item.sale_price * i.count_item)
            else:
                cart_total += (i.item.price * i.count_item)

        form = CreateOrder()

        return render(request, 'cart/cart.html', {'cart': cart, 'cart_total': cart_total, 'form': form})
    else:
        messages.info(request, ('Please login or register first!'))

        return redirect('/')


def additional_item(request, item_id, cart_id):
    item_in_cart = CartInfo.objects.get(cart=cart_id, item=item_id)
    item_in_cart.count_item +=1
    item_in_cart.save()

    return redirect('/cart')


def delete_additional_item(request, item_id, cart_id):
    item_in_cart = CartInfo.objects.get(cart=cart_id, item=item_id)
    item_in_cart.count_item -=1
    item_in_cart.save()

    return redirect('/cart')


def add_to_cart(request, item_id):
    if request.user.is_authenticated:
        if request.method == "GET":
            cart, created = Cart.objects.get_or_create(user_id=request.user.id)
            item = get_object_or_404(Item, id=item_id)
            #TODO change the method to POST
            CartInfo.objects.create(cart=cart, item = item, count_item=1)
            messages.success(request, ('You have added item to cart!'))
    else:
        messages.info(request, ('Please login or register first!'))

    return redirect('/')


def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user_id=request.user.id)
        item = get_object_or_404(Item, id=item_id)
        cart.cartinfo_set.filter(cart=cart, item=item).delete()
        return redirect('/cart')
    else:
        messages.info(request, ('Please login or register first!'))

    return redirect('/')
