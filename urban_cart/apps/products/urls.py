from django.urls import path
from . import views

urlpatterns = [
    path('',views.product_list,name='product_list'),
    path('product_details/<int:product_id>/',views.product_details,name='product_details'),
     path('product_category/<int:sub_category_id>/',views.product_category,name='product_category'),
     path('product_details/<int:rec_product_id>/',views.product_details,name='product_details'),
     
     

    #  path('category/',views.category_list,name="category_list_brand")
]
