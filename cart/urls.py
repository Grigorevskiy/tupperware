from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_cart, name = "get_cart"),
    path('add/<int:item_id>', views.add_to_cart, name = "add_to_cart"),
    path('remove/<int:item_id>', views.remove_from_cart, name = "remove_from_cart"),
    path('additional/<int:cart_id>/<int:item_id>', views.additional_item, name = "additional_item"),
    path('delete_additional/<int:cart_id>/<int:item_id>', views.delete_additional_item, name = "delete_additional_item"),

]
