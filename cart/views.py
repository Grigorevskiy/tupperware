from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from product.models import Item
from . forms import CreateOrder
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
        # form_info = Additional_order_info()

        if request.method == "POST":
            order = Order.objects.create(user=request.user, total=cart_total,
                                         delivery_address=request.POST['delivery_address'],
                                         contact_phone=request.POST['contact_phone'])


            for item in cart.item.all():
                order.items.add(item)

            cart.item.clear()
            messages.info(request, ('Thank you for your order, our manager will contact you soon!'))

            return redirect('/')

        return render(request, 'cart/cart.html', {'cart': cart, 'cart_total': cart_total, 'form': form})
    else:
        messages.info(request, ('Please login or register first!'))
        return redirect('/')


def additional_item(request, item_id):
    cart, created = Cart.objects.get_or_create(user_id=request.user.id)
    form = CreateOrder()

    s = OrderInfo.objects.get_or_create(item_id_id=item_id)

    s.count_item += 1


    cart_total = 0
    for i in cart.item.all():
        if s.count_item > 1:
            new_price = s.count_item * i.price
        if i.sale_price:
            cart_total += i.sale_price
        else:
            cart_total += i.price


    return render(request, 'cart/cart.html',
                  {'cart': cart, 'cart_total': cart_total, 'form': form, 'count': s.count_item})


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
