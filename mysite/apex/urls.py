from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<gender>/pg=<page>', views.initial_list, name='list'),
    path('<gender>/<category>/pg=<page>', views.further_list, name='further_list'),
    path('<gender>/<category>/a=<art_no>&l=<leather_1>', views.details, name='details'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    # path('user_save', views.user_save, name='user_save'),
    # path('<int:sl>/cart', views.cart, name='cart'),
    # path('<gender>/gender', views.gender_collections, name='gender_collections'),
    # path('gender', views.gender, name='gender'),
    # path('test_form', views.test, name='test'),


]