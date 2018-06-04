from django.shortcuts import render, redirect
from . forms import CreateOrder
from cart.models import Cart, CartInfo
from . models import Order, OrderInfo
from django.contrib import messages


def create_order(request):
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
        if request.method == "POST":
            order = Order.objects.create(user=request.user, total=cart_total,
                                         delivery_address=request.POST['delivery_address'],
                                         contact_phone=request.POST['contact_phone'])
            for i in cart.cartinfo_set.all():
                order_info = OrderInfo.count_item = CartInfo.objects.first().count_item
                order_info = OrderInfo(item_in_order=i.item)
                order_info.save()
                # order.item.add(item)

            cart.items.clear()
            messages.info(request, ('Thank you for your order, our manager will contact you soon!'))

            return redirect('/')
        return render(request, 'cart/cart.html', {'form': form, 'cart':cart, 'cart_total':cart_total})


    else:
        return redirect('/')
