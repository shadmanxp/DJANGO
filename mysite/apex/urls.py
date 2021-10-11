from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<gender>', views.list, name='list'),
    path('<gender>/<category>', views.further_list, name='further_list'),
    # path('<int:sl>/cart', views.cart, name='cart'),
    # path('<gender>/gender', views.gender_collections, name='gender_collections'),
    # path('gender', views.gender, name='gender'),

]