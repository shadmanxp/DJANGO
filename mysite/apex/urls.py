from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<gender>/pg=<page>', views.initial_list, name='list'),
    path('<gender>/<category>/pg=<page>', views.further_list, name='further_list'),
    path('<gender>/<category>/a=<art_no>&l=<leather_1>', views.details, name='details'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('addToCart/<sl>', views.addToCart, name='addToCart'),
    path('removeFromCart/<sl>', views.removeFromCart, name='removeFromCart'),
    path('updateCart/<sl>', views.updateCart, name='updatesCart'),
    path('placeOrder', views.placeOrder, name='placeOrder'),
    path('cart', views.cart, name='cart'),
    path('orders', views.viewOrders, name='viewOrders'),
    # path('user_save', views.user_save, name='user_save'),
    # path('<int:sl>/cart', views.cart, name='cart'),
    # path('<gender>/gender', views.gender_collections, name='gender_collections'),
    # path('gender', views.gender, name='gender'),
    # path('test_form', views.test, name='test'),


]