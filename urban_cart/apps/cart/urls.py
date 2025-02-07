from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart,name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/', views.update_cart, name='update_cart'),

]
