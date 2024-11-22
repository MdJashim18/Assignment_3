from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.Musicians, name='Musicians'),
    path('edit/<int:id>/', views.Edit_musicians, name='Edit_musicians'),
    path('delete/<int:id>/', views.delete_musicians, name='delete_musicians'),
]
