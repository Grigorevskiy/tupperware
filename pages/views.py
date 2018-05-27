from django.shortcuts import render

from product.models import Category, Item


def home(request):

    return render(request, 'home.html')


