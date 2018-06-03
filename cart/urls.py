from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_cart, name = "get_cart"),
    path('add/<int:item_id>', views.add_to_cart, name = "add_to_cart"),
    path('remove/<int:item_id>', views.remove_from_cart, name = "remove_from_cart"),
    path('additional/<int:item_id>', views.additional_item, name = "additional_item"),

]
