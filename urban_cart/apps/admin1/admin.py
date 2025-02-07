from django.contrib import admin
from apps.admin1.models import Product,Slider,MainCategory,SubCategory,Manufacturer

# Register your models here.
admin.site.register(Product),
admin.site.register(Slider),
admin.site.register(MainCategory),
admin.site.register(SubCategory),
admin.site.register(Manufacturer),