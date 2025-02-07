from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from datetime import timedelta
# Create your models here.
# Choices for Product Category
class MainCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return f"{self.name} ({self.main_category.name})"
    
class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    image_url = models.URLField()
    site_link = models.URLField()
    product_stock=models.PositiveIntegerField(default=100)
    ratings = models.FloatField(null=True, blank=True)
    no_of_ratings = models.PositiveIntegerField(null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
# class Slider(models.Model):
#     add_head = models.CharField(max_length=255, verbose_name="Heading")
#     add_sub_head = models.CharField(max_length=255, verbose_name="Subheading", blank=True, null=True)
#     add_text = models.TextField(verbose_name="Text Description", blank=True, null=True)
#     add_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price", blank=True, null=True)
#     add_image = models.ImageField(upload_to='slider_images/', verbose_name="Image")

#     def __str__(self):
#         return self.add_head
class Slider(models.Model):
    add_head = models.CharField(max_length=200)
    add_sub_head = models.CharField(max_length=200, default="Default Subheading")
    add_text = models.CharField(max_length=200, default="Default Text")
    add_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Default added here
    add_image = models.ImageField(upload_to='sliders/')
    start_time = models.DateTimeField(default=now)  # Default to current time
    end_time = models.DateTimeField(default=now() + timedelta(hours=4))  # Default to 4 hours after start_time
    def __str__(self):
        return f"{self.add_head} ({self.add_sub_head}) ({self.start_time}) ({self.end_time})"
