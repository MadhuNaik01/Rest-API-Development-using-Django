from django.urls import path
from graphviz import view
from . import views

urlpatterns = [
    path('api/<id>/', views.getData),
    path('', views.getData),
    path('add/', views.addData),
    path('delete/<id>/', views.deleteData),
    path('update/<id>/', views.updateData),
]
