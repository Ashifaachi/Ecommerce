# from django.db import models
# from apps.products.models import Product
# from apps.users.models import Register

# # Create your models here.
# class Cart(models.Model):
#     user = models.ForeignKey('users.Register', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     added_at = models.DateTimeField(auto_now_add=True)
from django.db import models
# from apps.products.models import Product  # Import the Product model directly
# from apps.users.models import Register  # Import the Register model directly

class Cart(models.Model):
    user = models.ForeignKey('users.Register', on_delete=models.CASCADE)  # Use Register directly
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart({self.user.username})"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('admin1.Product', on_delete=models.CASCADE)  # Use Product directly
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CartItem({self.product.name} - {self.quantity})"
