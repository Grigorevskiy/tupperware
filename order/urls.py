from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_order, name="create_order"),
]
