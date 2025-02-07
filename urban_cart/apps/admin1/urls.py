from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin_dashboard'),
    path('add_item/',views.add_item,name='add_item'),
    path('delete_item/',views.delete_item,name='delete_item'),
    path('list_item',views.list_item,name='list_item'),
    path('slide/',views.slide,name='slide'),
    path('update_item/',views.update_item,name='update_item'),
    path('edit_slide/', views.edit_slide, name='edit_slide'),
    path('delete_slide/', views.delete_slide, name='delete_slide'),
    # path('add_category/',views.add_category,name='add_category'),
    # path('delete_category/',views.delete_category,name='delete_category'),
   


]
