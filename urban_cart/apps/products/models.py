from django.db import models
from apps.admin1.models import Product
from apps.users.models import Register

# Create your models here.

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'Review by {self.user.name} on {self.product.name}'
