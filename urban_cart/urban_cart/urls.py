"""
URL configuration for urban_cart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings  
from django.conf.urls.static import static 



from django.conf.urls import handler404,handler500,handler403
from .views import custom_404_view,custom_500_view,custom_400_view,custom_403_view # Replace 'your_app' with your actual app name

handler404 = custom_404_view 
handler500 = custom_500_view 
handler403 = custom_403_view
handler400 = custom_400_view

urlpatterns = [
    path('admin/', admin.site.urls),
     path('products/',include('apps.products.urls')),
    path('users/',include('apps.users.urls')),
    path('cart/',include('apps.cart.urls')),
    path('orders/',include('apps.orders.urls')),
    path('payments/',include('apps.payments.urls')),
    path('',include('apps.home.urls')),
    path('admin1/',include('apps.admin1.urls')),
    path('accounts/', include('apps.users.urls')),  
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)