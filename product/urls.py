from django.urls import path
from product import views


urlpatterns = [
    path('<int:item_id>/comment/create', views.create_comment, name='create_comment'),
    path('<int:item_id>/comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
    path('<int:item_id>/comment/<int:comment_id>/update', views.update_comment, name='update_comment')
    ]
