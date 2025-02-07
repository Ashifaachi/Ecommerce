from django.db import models
from django.contrib.auth.models import User
from apps.users.models import State, District
from django.conf import settings
from apps.admin1.models import Product
# Create your models here.
# class Address(models.Model):
#     user = models.ForeignKey('users.Register', on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     address = models.TextField()
#     address2 = models.TextField(blank=True, null=True)
#     state = models.ForeignKey(State, on_delete=models.CASCADE)  
#     district = models.ForeignKey(District, on_delete=models.CASCADE)  
#     pin = models.CharField(max_length=10)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name} - {self.address}"
    
# class Payment(models.Model):
#     user = models.ForeignKey('users.Register', on_delete=models.CASCADE)
#     razorpay_order_id = models.CharField(max_length=100, unique=True)
#     razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
#     razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(
#         max_length=20,
#         choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')],
#         default='Pending'
#     )

#     def __str__(self):
#         return f"Payment {self.razorpay_order_id} - {self.user.username}"

# class Order(models.Model):
#     user = models.ForeignKey('users.Register', on_delete=models.CASCADE)
#     payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(
#         max_length=20,
#         choices=[('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')],
#         default='Processing'
#     )

#     def __str__(self):
#         return f"Order {self.id} - {self.user.username}"

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
class Address(models.Model):
    user = models.ForeignKey('users.Register', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    address2 = models.TextField(blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    pin = models.CharField(max_length=10)

class Order(models.Model):
    user = models.ForeignKey('users.Register', on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)