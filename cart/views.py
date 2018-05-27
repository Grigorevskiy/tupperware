from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from product.models import Item


def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user_id=request.user.id)
        # calculate total for price in cart items
        cart_total = 0
        for i in cart.item.all():
            if i.sale_price:
                cart_total += i.sale_price
            else:
                cart_total += i.price

        return render(request, 'cart/cart.html', {'cart': cart, 'cart_total': cart_total})
    else:
        messages.info(request, ('Please login or register first!'))
        return redirect('/')


def add_to_cart(request, item_id):
    if request.user.is_authenticated:
        if request.method == "GET":
            cart, created = Cart.objects.get_or_create(user_id=request.user.id)
            item = get_object_or_404(Item, id=item_id)
            cart.item.add(item)
            messages.success(request, ('You have added item to cart!'))
    else:
        messages.info(request, ('Please login or register first!'))
    return redirect('/')


def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user_id=request.user.id)
        item = get_object_or_404(Item, id=item_id)
        cart.item.remove(item)
        return redirect('/cart')

    else:
        messages.info(request, ('Please login or register first!'))
    return redirect('/')
