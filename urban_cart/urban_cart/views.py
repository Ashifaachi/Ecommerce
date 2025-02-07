from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, 'urban_cart/404.html', status=404)

def custom_500_view(request):  # Remove exception parameter
    return render(request, 'urban_cart/500.html', status=500)

def custom_403_view(request, exception):
    return render(request, 'urban_cart/403.html', status=403)

def custom_400_view(request, exception):
    return render(request, 'urban_cart/400.html', status=400)


