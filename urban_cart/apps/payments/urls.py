from django.urls import path
from .views import payment_cancel,payment_success,checkout,add_address,payment_failed,get_districts

urlpatterns = [
    path("checkout/", checkout, name="checkout"),
    path("success/", payment_success, name="payment_success"),
    path("payment_cancel/", payment_failed, name="payment_failed"),
    path("add_address/", add_address, name="add_address"),
    path('get-districts/<int:state_id>/', get_districts, name='get_districts'),

]
