from django.shortcuts import render


from pages.models import Faq


from product.models import Category, Item, SliderPhoto



def home(request):
    items = Item.objects.exclude(status=0)[:12]
    slider = SliderPhoto.objects.all()
    return render(request, 'home.html', {'items': items, 'slider': slider})

def about_us(request):

    return render(request, 'about_us.html')


def delivery(request):
    return render(request, 'delivery.html')


def faq(request):
    faq_content = Faq.objects.all()
    return render(request, 'faq.html', {'faq_content': faq_content,})

def search(request):
    categories = Category.objects.all()
    query_item_name = request.GET.get('q')
    query_category_id = request.GET.get('category_id')
    if query_category_id:
        items = Item.objects.exclude(status=0).filter(category=query_category_id, title__icontains=query_item_name)
        return render(request, 'home.html', {'items': items, 'categories': categories, 'query_item_name':query_item_name, 'query_category_id':query_category_id})
    else:
        items = Item.objects.exclude(status=0).filter(title__icontains=query_item_name)
        return render(request, 'home.html', {'items': items, 'categories': categories, 'query_item_name':query_item_name})
