from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from product.models import Item
from . forms import CreateOrder, Additional_order_info
from order.models import Order, OrderInfo


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

        form = CreateOrder()
        form_info = Additional_order_info()


        if request.method == "POST":
            order = Order.objects.create(user=request.user, total=cart_total,
                                         delivery_address=request.POST['delivery_address'],
                                         contact_phone=request.POST['contact_phone'])

            for item in cart.item.all():
                order.items.add(item)

            cart.item.clear()
            messages.info(request, ('Thank you for your order, our manager will contact you soon!'))

            return redirect('/')

        return render(request, 'cart/cart.html', {'cart': cart, 'cart_total': cart_total, 'form': form, 'form_info' : form_info})
    else:
        messages.info(request, ('Please login or register first!'))
        return redirect('/')


def add_additional_item(request, item_id):
    if request.user.is_authenticated:
        if request.method == "GET":
            cart, created = Cart.objects.get(user_id=request.user.id)
            item = get_object_or_404(Item, id=item_id)
            cart.item.add(item)
            messages.success(request, ('You have added item to cart!'))
    else:
        messages.info(request, ('Please login or register first!'))

    return render(request, '')


def remove_additional_item(request, item_id):


    return render(request, '')


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
