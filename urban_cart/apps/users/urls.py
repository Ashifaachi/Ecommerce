from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('abcdf/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    # path('account/',views.account,name='account'),
    # path('logout/', views.logout, name='logout'),
    # path('', auth_views.LoginView.as_view(), name='login'),
    path('login/', views.login, name='login'),  # Custom login view
    path('logout/', views.logout, name='logout'),  # Custom logout view
    path('account/', views.account, name='update_address'),  # Example account page
    path('register/', views.register, name='register'),
    


]
