from django.shortcuts import render
from apps.admin1.models import Slider,Product,SubCategory
from django.http import JsonResponse
from collections import Counter
from django.utils.timezone import now
from datetime import timedelta
from datetime import datetime

from apps.cart.models import CartItem
from itertools import islice
import pandas as pd
from django.shortcuts import render, get_object_or_404
import random


# Create your views here.
from django.shortcuts import render, get_object_or_404


# def index(request):
#    sliders = Slider.objects.all()
#    if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))[:10]
#         titles = list()
#         for product in qs:
#             titles.append(product.name)
#         return JsonResponse(titles,safe=False)
   
    
  
#    all_products=Product.objects.all()
#    all_brands=[]

#    for product in all_products:

#     all_brands.append(product.name.split()[0:5])
    
#     count_brand = Counter(all_brands)


#     data = count_brand.items()
#     context = {
#         'data': data,
#         'sliders': sliders
#         }
#    return render(request, 'home/index.html',context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.all()

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')  # Default to an empty string if term is not provided
#         qs = Product.objects.filter(name__icontains=search_term)[:10]  # Limit to 10 results
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # Extract brand names (assuming the first word of the product name is the brand)
#     all_brands = [product.name.split()[0] for product in all_products if product.name]  # Avoid splitting None or empty names

#     # Count brand occurrences
#     count_brand = Counter(all_brands)[:5]

#     # Prepare data for context
#     data = count_brand.items()
#     context = {
#         'data': data,
#         'sliders': sliders
#     }

#     # Render the home page
#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')
#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')  # Default to an empty string if term is not provided
#         qs = Product.objects.filter(name__icontains=search_term)[:10]  # Limit to 10 results
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # Extract brand names (assuming the first word of the product name is the brand)
#     all_brands = [product.name.split()[0] for product in all_products if product.name]  # Avoid splitting None or empty names

#     # Count brand occurrences
#     count_brand = Counter(all_brands)

#     # Filter brands with count > 500 and limit to the top 4 items
#     filtered_brands = [(brand, count) for brand, count in count_brand.items() if count > 500]
#     filtered_brands = sorted(filtered_brands, key=lambda x: x[1], reverse=True)[:4]

#     # Prepare data for context
#     context = {
#         'data': filtered_brands,
#         'sliders': sliders
#     }

#     # Render the home page
#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # Extract brand names (assuming the first word of the product name is the brand)
#     all_brands = [product.name.split()[0] for product in all_products if product.name]
#     count_brand = Counter(all_brands)

#     # Filter brands with count > 500 and limit to the top 4
#     filtered_brands = sorted([(brand, count) for brand, count in count_brand.items() if count > 500], 
#                              key=lambda x: x[1], reverse=True)[:4]

#     # ** Fetch recommendations **
#     recommended_products = []
    
#     if request.user.is_authenticated:
#         user_id = request.user.id  # Get the logged-in user's ID
#         user_cart_items = CartItem.objects.filter(cart__user_id=user_id).values_list('product__id', flat=True)

#         if user_cart_items:
#             # Get collaborative filtering recommendations
#             recommended_products = collaborative_filtering_recommendations(all_products, user_id, top_n=8)
#         else:
#             # Fallback to rating-based recommendations if no user history
#             recommended_products = all_products.order_by('-ratings')[:8]

#     # Prepare context
#     context = {
#         'data': filtered_brands,
#         'sliders': sliders,
#         'recommended_products': recommended_products,  # Pass recommendations to template
#     }

#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # Extract brand names (assuming the first word of the product name is the brand)
#     all_brands = [product.name.split()[0] for product in all_products if product.name]
#     count_brand = Counter(all_brands)

#     # Filter brands with count > 500 and limit to the top 4
#     filtered_brands = sorted([(brand, count) for brand, count in count_brand.items() if count > 500], 
#                              key=lambda x: x[1], reverse=True)[:4]

#     # ** Fetch recommendations **
#     recommended_products = []

#     if request.user.is_authenticated:
#         user_id = request.user.id  # Get the logged-in user's ID
#         user_cart_items = CartItem.objects.filter(cart__user_id=user_id).values_list('product__id', flat=True)

#         if user_cart_items:
#             # Get collaborative filtering recommendations
#             recommended_products = collaborative_filtering_recommendations(all_products, user_id, top_n=8)

#             # ✅ Ensure it's a list
#             if isinstance(recommended_products, Product):  
#                 recommended_products = [recommended_products]  # Convert single object to list
#         else:
#             # Fallback to rating-based recommendations if no user history
#             recommended_products = list(all_products.order_by('-ratings')[:8])  # ✅ Convert to list

#     # Prepare context
#     context = {
#         'data': filtered_brands,
#         'sliders': sliders,
#         'recommended_products': recommended_products,  # Pass recommendations to template
#     }

#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # Extract brand names (assuming the first word of the product name is the brand)
#     all_brands = [product.name.split()[0] for product in all_products if product.name]
#     count_brand = Counter(all_brands)

#     # Filter brands with count > 500 and limit to the top 4
#     filtered_brands = sorted([(brand, count) for brand, count in count_brand.items() if count > 500], 
#                              key=lambda x: x[1], reverse=True)[:4]

#     # ** Fetch recommendations **
#     recommended_products = []

#     if request.user.is_authenticated:
#         user_id = request.user.id  # Get the logged-in user's ID
#         user_cart_items = CartItem.objects.filter(cart__user_id=user_id).values_list('product__id', flat=True)

#         if user_cart_items:
#             # Get collaborative filtering recommendations
#             recommended_products = collaborative_filtering_recommendations(all_products, user_id, top_n=8)

#             # ✅ Ensure it's always a list
#             if isinstance(recommended_products, Product):  # Check if single product is returned
#                 recommended_products = [recommended_products]  # Wrap single product in a list
#         else:
#             # Fallback to rating-based recommendations if no user history
#             recommended_products = list(all_products.order_by('-ratings')[:8])  # Convert to list if QuerySet

#     # Prepare context
#     context = {
#         'data': filtered_brands,
#         'sliders': sliders,
#         'recommended_products': recommended_products,  # Pass recommendations to template
#     }

#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # Extract brand names (assuming the first word of the product name is the brand)
#     all_brands = [product.name.split()[0] for product in all_products if product.name]
#     count_brand = Counter(all_brands)

#     # Filter brands with count > 500 and limit to the top 4
#     filtered_brands = sorted([(brand, count) for brand, count in count_brand.items() if count > 500], 
#                              key=lambda x: x[1], reverse=True)[:4]

#     # Fetch recommendations
#     recommended_products = []

#     if request.user.is_authenticated:
#         user_id = request.user.id
#         user_cart_items = CartItem.objects.filter(cart__user_id=user_id).values_list('product__id', flat=True)

#         if user_cart_items:
#             recommended_products = collaborative_filtering_recommendations(all_products, user_id, top_n=8)
#         else:
#             recommended_products = list(all_products.order_by('-ratings')[:8])

#     # Ensure `recommended_products` is always a list
#     if isinstance(recommended_products, Product):  # Check if a single product is returned
#         recommended_products = [recommended_products]  # Wrap single product in a list
#     elif not isinstance(recommended_products, list):  # In case it's not a list
#         recommended_products = list(recommended_products)  # Convert to a list

#     # Split `recommended_products` into chunks of 3 for the carousel
#     def chunked(iterable, size):
#         it = iter(iterable)
#         return list(iter(lambda: list(islice(it, size)), []))

#     recommended_products_chunks = chunked(recommended_products, 3)

#     # Prepare context
#     context = {
#         'data': filtered_brands,
#         'sliders': sliders,
#         'recommended_products': recommended_products_chunks,  # Pass chunked recommendations to template
#     }

#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # Extract brand names (assuming the first word of the product name is the brand)
#     all_brands = [product.name.split()[0] for product in all_products if product.name]
#     count_brand = Counter(all_brands)

#     # Filter brands with count > 500 and limit to the top 4
#     filtered_brands = sorted([(brand, count) for brand, count in count_brand.items() if count > 500], 
#                              key=lambda x: x[1], reverse=True)[:4]

#     # Fetch recommendations
#     recommended_products = []

#     if request.user.is_authenticated:
#         user_id = request.user.id  # Get the logged-in user's ID
#         user_cart_items = CartItem.objects.filter(cart__user_id=user_id).values_list('product__id', flat=True)

#         if user_cart_items:
#             # Get collaborative filtering recommendations
#             recommended_products = collaborative_filtering_recommendations(all_products, user_id, top_n=8)
#         else:
#             # Fallback to rating-based recommendations if no user history
#             recommended_products = list(all_products.order_by('-ratings')[:8])  # Convert to list if QuerySet

#     # Prepare context
#     context = {
#         'data': filtered_brands,
#         'sliders': sliders,
#         'recommended_products': recommended_products,  # Pass recommendations to template
#     }

#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # Extract brand names (assuming the first word of the product name is the brand)
#     all_brands = [product.name.split()[0] for product in all_products if product.name]
#     count_brand = Counter(all_brands)

#     # Filter brands with count > 500 and limit to the top 4
#     filtered_brands = sorted([(brand, count) for brand, count in count_brand.items() if count > 500], 
#                              key=lambda x: x[1], reverse=True)[:4]

#     # ** Fetch recommendations **
#     recommended_products = []

#     if request.user.is_authenticated:
#         user_id = request.user.id  # Get the logged-in user's ID
#         user_cart_items = CartItem.objects.filter(cart__user_id=user_id).values_list('product__id', flat=True)

#         if user_cart_items:
#             # Get collaborative filtering recommendations (no need to pass top_n if it's a default argument)
#             recommended_products = collaborative_filtering_recommendations(all_products, user_id)

#             # Ensure `recommended_products` is always a list
#             if isinstance(recommended_products, Product):  # Check if a single product is returned
#                 recommended_products = [recommended_products]  # Wrap single product in a list
#             elif not isinstance(recommended_products, list):  # In case it's not a list
#                 recommended_products = list(recommended_products)  # Convert to a list
#         else:
#             # Fallback to rating-based recommendations if no user history
#             recommended_products = list(all_products.order_by('-ratings')[:8])  # Convert to list if QuerySet

#     # Prepare context
#     context = {
#         'data': filtered_brands,
#         'sliders': sliders,
#         'recommended_products': recommended_products,  # Pass recommendations to template
#     }

#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # Extract brand names (assuming the first word of the product name is the brand)
#     all_brands = [product.name.split()[0] for product in all_products if product.name]
#     count_brand = Counter(all_brands)

#     # Filter brands with count > 500 and limit to the top 4
#     filtered_brands = sorted([(brand, count) for brand, count in count_brand.items() if count > 500], 
#                              key=lambda x: x[1], reverse=True)[:4]

#     # ** Fetch recommendations **
#     recommended_products = []

#     if request.user.is_authenticated:
#         user_id = request.user.id  # Get the logged-in user's ID
#         user_cart_items = CartItem.objects.filter(cart__user_id=user_id).values_list('product__id', flat=True)

#         if user_cart_items:
#             # Get hybrid recommendations (using both content-based and collaborative filtering)
#             recommended_products = hybrid_recommendations(user_id, all_products.first().name)  # Example using first product's name

#             # Ensure `recommended_products` is always a list
#             if isinstance(recommended_products, Product):  # Check if a single product is returned
#                 recommended_products = [recommended_products]  # Wrap single product in a list
#             elif not isinstance(recommended_products, list):  # In case it's not a list
#                 recommended_products = list(recommended_products)  # Convert to a list
#         else:
#             # Fallback to rating-based recommendations if no user history
#             recommended_products = list(all_products.order_by('-ratings')[:8])  # Convert to list if QuerySet

#     # Prepare context
#     context = {
#         'data': filtered_brands,
#         'sliders': sliders,
#         'recommended_products': recommended_products,  # Pass recommendations to template
#     }

#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # ** Fetch recommendations **
#     recommended_products = []

#     if request.user.is_authenticated:
#         user_id = request.user.id  # Get the logged-in user's ID

#         # Use the hybrid recommendation system
#         recommended_products = hybrid_recommendations(user_id, all_products.first().name)  # Example using first product's name

#     # Prepare context
#     context = {
#         'sliders': sliders,
#         'recommended_products': recommended_products,  # Pass recommendations to template
#     }

#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # ** Fetch recommendations **
#     recommended_products = []

#     if request.user.is_authenticated:
#         user_id = request.user.id  # Get the logged-in user's ID

#         # Use the hybrid recommendation system
#         content_recs = hybrid_recommendations(user_id, all_products.first().name)  # Example using first product's name
#         collaborative_recs = collaborative_filtering_recommendations(user_id)

#         if collaborative_recs.empty:
#             print("Using content-based recommendations only.")
#             recommended_products = content_recs  # Fallback to content-based recommendations
#         else:
#             # Combine content-based and collaborative recommendations, removing duplicates
#             recommended_products = pd.concat([content_recs, collaborative_recs]).drop_duplicates()

#     # Prepare context
#     context = {
#         'sliders': sliders,
#         'recommended_products': recommended_products,  # Pass recommendations to template
#     }

#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

#     # Fetch content-based recommendations for the first product (example)
#     recommended_products = []
#     if all_products.exists():
#         first_product_name = all_products.first().name
#         recommended_products = content_based_recommendations(first_product_name, top_n=10)

#     # Prepare context
#     context = {
#         'sliders': sliders,
#         'recommended_products': recommended_products,  # Pass recommendations to template
#     }

#     return render(request, 'home/index.html', context)
# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Check for 'term' in GET request for search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Retrieve all products
#     all_products = Product.objects.all()

    

#     # Prepare context
#     context = {
#         'sliders': sliders,
        
#     }

#     return render(request, 'home/index.html', context)


def sEarch(request):
    
    
    return render(request,'home/index.html')


# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Handle search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Get products for each subcategory
#     subcategory_products = []
    
#     # Get all subcategories
#     subcategories = SubCategory.objects.all()
    
#     for subcategory in subcategories:
#         products = Product.objects.filter(sub_category=subcategory)
#         if products.exists():
#             # Group products into chunks of 3 for carousel slides
#             products_list = list(products)
#             product_chunks = [products_list[i:i+3] for i in range(0, len(products_list), 3)]
            
#             subcategory_products.append({
#                 'name': subcategory.name,
#                 'products': products_list,

#                 'product_chunks': product_chunks
#             })

#     context = {
#         'sliders': sliders,
#         'subcategory_products': subcategory_products,
#     }

#     return render(request, 'home/index.html', context)

# def index(request):
#     # Fetch slider data
#     sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

#     # Handle search functionality
#     if 'term' in request.GET:
#         search_term = request.GET.get('term', '')
#         qs = Product.objects.filter(name__icontains=search_term)[:10]
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Get products for each subcategory
#     subcategory_products = []
    
#     # Get all subcategories
#     subcategories = SubCategory.objects.all()
    
#     for subcategory in subcategories:
#         products = Product.objects.filter(sub_category=subcategory)
#         if products.exists():
#             # Get all products without chunking
#             subcategory_products.append({
#                 'name': subcategory.name,
#                 'products': products
#             })

#     context = {
#         'sliders': sliders,
#         'subcategory_products': subcategory_products,
#     }

#     return render(request, 'home/index.html', context)

def index(request):
    # Fetch slider data
    sliders = Slider.objects.filter(end_time__gte=datetime.now()).order_by('-end_time')

    # Handle search functionality
    if 'term' in request.GET:
        search_term = request.GET.get('term', '')
        qs = Product.objects.filter(name__icontains=search_term)[:10]
        titles = [product.name for product in qs]
        return JsonResponse(titles, safe=False)

    # Get products for each subcategory
    subcategory_products = []
    
    # Get all subcategories
    subcategories = SubCategory.objects.all()
    
    for subcategory in subcategories:
        # Get all products for this subcategory
        products = list(Product.objects.filter(sub_category=subcategory))
        
        if products:
            # Shuffle the products randomly
            random.shuffle(products)
            
            # Take only first 12 products
            products = products[:12]
            
            # Group products into chunks of 3 for carousel slides
            product_chunks = [products[i:i+3] for i in range(0, len(products), 3)]
            
            subcategory_products.append({
                'name': subcategory.name,
                'products': products,
                'product_chunks': product_chunks
            })

    context = {
        'sliders': sliders,
        'subcategory_products': subcategory_products,
    }

    return render(request, 'home/index.html', context)

