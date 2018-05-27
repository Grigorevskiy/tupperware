from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('delivery/', views.delivery, name='delivery'),
    path('faq/', views.faq, name='faq'),
    path('search/', views.search, name='search'),
]
