from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_wishlist, name="get_wishlist"),
    path('add_wish/<int:item_id>', views.add_to_wishlist, name="add_to_wishlist"),
    path('remove_wish/<int:item_id>', views.remove_from_wishlist, name="remove_from_wishlist"),
    ]
