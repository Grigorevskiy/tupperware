from django.urls import path
from product import views



urlpatterns = [
    path('<int:category_id>/', views.category_detail, name='category_detail'),
]