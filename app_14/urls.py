from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe/', views.recipe, name='recipe'),
    path('getdata/', views.getdata, name='getdata'),
    path('table/', views.table, name='table'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]