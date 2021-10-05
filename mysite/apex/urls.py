from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sl>', views.detail, name='detail'),
    path('<int:sl>/cart', views.cart, name='cart'),
    path('<gender>/gender', views.gender_collections, name='gender_collections'),
    path('gender', views.gender, name='gender'),

]