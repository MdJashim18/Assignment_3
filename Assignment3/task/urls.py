from django.urls import path
from .import views
urlpatterns = [
    path('add/',views.task,name='add_task'),
    path('edit/<int:id>/',views.Edit_task,name='Edit_task'),
    path('delete/<int:id>/',views.delete_task,name='delete_task'),
    path('show/',views.Show_task,name='Show_task'),
    path('complete/<int:id>/', views.complete_task, name='complete_task'),
]