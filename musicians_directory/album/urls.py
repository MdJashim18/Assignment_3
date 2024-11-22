from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.Album, name='Album'),
    path('edit/<int:id>/', views.Edit_Album, name='Edit_Album'),
    path('delete/<int:id>/', views.delete_album, name='delete_album'),  
]
