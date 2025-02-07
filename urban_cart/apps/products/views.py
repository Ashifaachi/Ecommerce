from django.shortcuts import render,redirect
from apps.admin1.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
# Create your views here.
from django.shortcuts import render, get_object_or_404
from collections import Counter
from django.db.models import F
from django.contrib.auth.decorators import login_required
from apps.users.models import Register
from apps.home.recommendations import get_recommendations
from .models import Review


# def product_list(request):
#     products = Product.objects.all()
#     if request.method == 'POST':  # Handle input quantity
#         product_id = request.POST.get('product_id')  # Get the book ID from the form
#         product_stock = request.POST.get('product_stock')  # Quantity from the form

#         try:
#             product_stock = int(product_stock)  # Convert quantity to integer
#         except ValueError:
#             product_stock = 0

#         if product_stock > 0:
#             try:
#                 # Retrieve the specific book by its primary key (id)
#                 product = Product.objects.get(id=product_id)

#                 # Check if there's enough stock
#                 if product.product_stock < product_stock:
#                     error_message = "Not enough stock available."
#                     return render(request, 'user_list.html', {'product': product, 'error_message': error_message})

#                 # Calculate the total price
#                 total_price = product.product_price * product_stock

#                 # Deduct the quantity from the actual stock
#                 product.product_stock -= product_stock
#                 product.save()  # Save the updated quantity

#                 # Prepare context to display the selected book info
#                 context = {
#                     'product_name': product.product_name,
#                     'product_description': product.product_description,
#                     'product_image1': product.product_image1,
#                     'product_image2': product.product_image2,
#                     'product_image3': product.product_image3,
#                     'product_category': product.product_category,
#                     'product_stock': product_stock,
#                     'product_price': total_price,
#                 }

#                 return render(request, 'cart.html', context)  # Redirect to the cart page

#             except Product.DoesNotExist:
#                 error_message = "Book not found."
#                 return render(request, 'cart/cart.html', {'product': product, 'error_message': error_message})
#     return render(request, 'products/product_list.html',{'products':products})
# def product_list(request):
#     # Fetch all products to display in the product list
#     products = Product.objects.all()

#     if request.method == 'POST':  # Handle adding to cart with input quantity
#         product_id = request.POST.get('product_id')  # Get the product ID from the form
#         product_stock = request.POST.get('product_stock')  # Quantity from the form

#         try:
#             product_stock = int(product_stock)  # Convert quantity to an integer
#         except ValueError:
#             product_stock = 0  # Default to 0 if the input is invalid

#         if product_stock > 0:
#             try:
#                 # Retrieve the specific product by its primary key (id)
#                 product = Product.objects.get(id=product_id)

#                 # Check if there's enough stock available
#                 if product.product_stock < product_stock:
#                     error_message = "Not enough stock available."
#                     return render(
#                         request,
#                         'products/product_list.html',
#                         {'products': products, 'error_message': error_message}
#                     )

#                 # Calculate the total price
#                 total_price = product.product_price * product_stock

#                 # Deduct the quantity from the actual stock
#                 product.product_stock -= product_stock
#                 product.save()  # Save the updated stock

#                 # Prepare context to display the selected product details in the cart
#                 context = {
#                     'product_name': product.product_name,
#                     'product_description': product.product_description,
#                     'product_image1': product.product_image1,
#                     'product_image2': product.product_image2,
#                     'product_image3': product.product_image3,
#                     'product_category': product.product_category,
#                     'product_stock': product_stock,
#                     'product_price': total_price,
#                 }

#                 # Redirect to the cart page with the selected product details
#                 return render(request, 'cart/cart.html', context)

#             except Product.DoesNotExist:
#                 error_message = "Product not found."
#                 return render(
#                     request,
#                     'products/product_list.html',
#                     {'products': products, 'error_message': error_message}
#                 )

#     # Render the product list page with all products
#     return render(request, 'products/product_list.html', {'products': products})
# def product_list(request):
#     # Fetch all products
#     products_list = Product.objects.all()
#     all_products=Product.objects.all()
#     all_brands=[]

#     for product in all_products:
#         all_brands.append(product.name.split()[0])
    
#     count_brand = Counter(all_brands)


#     data = count_brand.items()

#     # Pagination setup: 10 products per page
#     paginator = Paginator(products_list, 9)
#     page = request.GET.get('page')  # Get the current page number from the request
    
#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver the first page
#         products = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range, deliver the last page of results
#         products = paginator.page(paginator.num_pages)
        
#     search = request.POST.get('search')
#     # Validate the item exists
#     if not Product.objects.filter(name=search).exists():
        
#         error_message = f"No products found in the '{search}' category."
#         return render(request, 'products/product_category.html', {'error_message': error_message})

#     # Fetch products for the given item
#     search_products = Product.objects.filter(name=search)


#     if request.method == 'POST':  # Handle adding to cart with input quantity

#         product_id = request.POST.get('product_id')  # Get the product ID from the form
#         product_stock = request.POST.get('product_stock')  # Quantity from the form
       

#         try:
#             product_stock = int(product_stock)  # Convert quantity to an integer
#         except ValueError:
#             product_stock = 0  # Default to 0 if the input is invalid

#         if product_stock > 0:
#             try:
#                 # Retrieve the specific product by its primary key (id)
#                 product = Product.objects.get(id=product_id)

#                 # Check if there's enough stock available
#                 if product.product_stock < product_stock:
#                     error_message = "Not enough stock available."
#                     return render(
#                         request,
#                         'products/product_list.html',
#                         {'products': products, 'error_message': error_message}
#                     )

#                 # Calculate the total price
#                 total_price = product.product_price * product_stock

#                 # Deduct the quantity from the actual stock
#                 product.product_stock -= product_stock
#                 product.save()  # Save the updated stock

#                 # Prepare context to display the selected product details in the cart
#                 context = {
#                     'name': product.name,
#                     'manufacturer': product.manufacturer,
#                     'main_category': product.main_category,
#                     'sub_category': product.sub_category,
#                     'image_url': product.image_url,
#                     'ratings': product.ratings,
#                     'product_stock': product_stock,
#                     'no_of_ratings':Product.no_of_ratings,
#                     'discount_price':Product.discount_price,
#                     'actual_price':Product.actual_price,
#                     'product_price': total_price,
#                 }

#                 # Redirect to the cart page with the selected product details
#                 return render(request, 'cart/cart.html', context)

#             except Product.DoesNotExist:
#                 error_message = "Product not found."
#                 return render(
#                     request,
#                     'products/product_list.html',
#                     {'products': products, 'error_message': error_message}
#                 )

#     # Render the product list page with paginated products
#     context = {
#         'data': data,
#         'products': products,
#         'search_products':search_products
#         }
#     return render(request, 'products/product_list.html',context)

# def product_list(request):
#     # Fetch all products
#     products_list = Product.objects.all()
    
#     # Get all brand names
#     all_brands = Product.objects.values_list('name', flat=True)
#     all_brands = [name.split()[0] for name in all_brands]
#     count_brand = Counter(all_brands)
#     data = count_brand.items()

#     # Pagination setup: 9 products per page
#     paginator = Paginator(products_list, 12)
#     page = request.GET.get('page')  # Get the current page number from the request

#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)  # If page is not an integer, show the first page
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)  # If out of range, show the last page

#     # Handle search functionality
#     search = request.POST.get('search')
#     if search:
#         search_products = Product.objects.filter(name__icontains=search)
#         if not search_products.exists():
#             error_message = f"No products found for '{search}'."
#             return render(request, 'products/product_category.html', {'error_message': error_message})
#     else:
#         search_products = None

#     # Handle adding to cart
#     if request.method == 'POST':  # Handle POST request
#         product_id = request.POST.get('product_id')  # Product ID from form
#         product_stock = request.POST.get('product_stock')  # Quantity from form
#         # Validate that product_id is a number
#         if not product_id.isdigit():
#             messages.error(request, "Invalid product ID.")
#             return redirect('product_list')  # Redirect to product list page
        

#         try:
#             product_stock = int(product_stock)  # Convert to integer
#         except (ValueError, TypeError):
#             product_stock = 0  # Default to 0 if invalid

#         if product_stock > 0 and product_id:
#             try:
#                 product = Product.objects.get(id=product_id)

#                 # Check if stock is sufficient
#                 if product.product_stock < product_stock:
#                     error_message = "Not enough stock available."
#                     return render(request, 'products/product_list.html', {'products': products, 'error_message': error_message})
                

#                 total_price = product.discount_price * product_stock

#                 # Update stock atomically
#                 product.product_stock = F('product_stock') - product_stock
#                 product.save()

#                 # Prepare cart context
#                 context = {
#                     'name': product.name,
#                     'manufacturer': product.manufacturer,
#                     'main_category': product.main_category,
#                     'sub_category': product.sub_category,
#                     'image_url': product.image_url,
#                     'ratings': product.ratings,
#                     'product_stock': product_stock,
#                     'no_of_ratings': product.no_of_ratings,
#                     'discount_price': product.discount_price,
#                     'actual_price': product.actual_price,
#                     'product_price': total_price,
#                 }
#                 return render(request, 'cart/cart.html', context)

#             except Product.DoesNotExist:
#                 error_message = "Product not found."
#                 return render(request, 'products/product_list.html', {'products': products, 'error_message': error_message})

#     # Render the product list
#     context = {
#         'data': data,
#         'products': products,
#         'search_products': search_products,
#     }

#     return render(request, 'products/product_list.html', context)
# def product_list(request):
#     # Fetch all products
#     products_list = Product.objects.all()

#     # Pagination setup: 12 products per page
#     paginator = Paginator(products_list, 12)
#     page = request.GET.get('page')

#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)

#     # Handle search functionality
#     search = request.POST.get('search')
#     if search:
#         search_products = Product.objects.filter(name__icontains=search)
#         if not search_products.exists():
#             error_message = f"No products found for '{search}'."
#             return render(request, 'products/product_list.html', {'error_message': error_message, 'products': products})
#     else:
#         search_products = None

#     # Handle adding to cart
#     if request.method == 'POST':  # POST request for adding to cart
#         product_id = request.POST.get('product_id')
#         product_quantity = request.POST.get('quantity', 1)  # Default quantity is 1

#         try:
#             product = Product.objects.get(id=product_id)

#             # Initialize the session cart if it doesn't exist
#             if 'cart' not in request.session:
#                 request.session['cart'] = {}

#             cart = request.session['cart']

#             # Update the cart
#             if product_id in cart:
#                 cart[product_id]['quantity'] += int(product_quantity)
#             else:
#                 cart[product_id] = {
#                     'name': product.name,
#                     'image_url': product.image_url,
#                     'price': product.discount_price,
#                     'quantity': int(product_quantity),
#                 }

#             # Save the updated cart back to the session
#             request.session['cart'] = cart
#             request.session.modified = True  # Mark the session as modified to save changes

#             return redirect('cart')  # Redirect to the cart page

#         except Product.DoesNotExist:
#             error_message = "Product not found."
#             return render(request, 'products/product_list.html', {'products': products, 'error_message': error_message})

#     context = {
#         'products': products,
#         'search_products': search_products,
#     }
#     return render(request, 'products/product_list.html', context)
# Product list view
def product_list(request):
    # Fetch all products
    products_list = Product.objects.all()
    # Pagination setup: 12 products per page
    paginator = Paginator(products_list, 12)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    # Handle search functionality
    search = request.POST.get('search')
    if search:
        search_products = Product.objects.filter(name__icontains=search)
        if not search_products.exists():
            error_message = f"No products found for '{search}'."
            return render(request, 'products/product_category.html', {'error_message': error_message})
    else:
        search_products = None

    

    context = {
        'products': products,
        'search_products': search_products,
    }
    return render(request, 'products/product_list.html', context)
# Add to cart view
# def add_to_cart(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         product_quantity = int(request.POST.get('product_stock', 1))  # Default to 1 if quantity is not provided

#         # Validate product_id and quantity
#         if not product_id.isdigit() or product_quantity < 1:
#             messages.error(request, "Invalid product ID or quantity.")
#             return redirect('product_list')

#         product = get_object_or_404(Product, id=product_id)

#         # Check stock availability
#         if product.product_stock < product_quantity:
#             messages.error(request, f"Only {product.product_stock} items available for {product.name}.")
#             return redirect('product_list')

#         # Update session cart
#         cart = request.session.get('cart', {})
#         cart[product_id] = cart.get(product_id, 0) + product_quantity
#         request.session['cart'] = cart

#         # Deduct stock
#         product.product_stock = F('product_stock') - product_quantity
#         product.save()
#         messages.success(request, f"{product_quantity} x {product.name} added to cart!")
#         return redirect('product_list')
# def add_to_cart(request):
#     if request.method == "POST":
#         product_id = request.POST.get("product_id")
#         quantity = request.POST.get("product_stock")

#         try:
#             quantity = int(quantity)
#         except (ValueError, TypeError):
#             messages.error(request, "Invalid quantity entered.")
#             return redirect("product_list")

#         if quantity <= 0:
#             messages.error(request, "Quantity must be greater than zero.")
#             return redirect("product_list")

#         # Fetch the product
#         product = get_object_or_404(Product, id=product_id)

#         if product.product_stock < quantity:
#             messages.error(request, "Not enough stock available.")
#             return redirect("product_list")

#         # Update session cart
#         cart = request.session.get("cart", {})
#         cart[product_id] = cart.get(product_id, 0) + quantity
#         request.session["cart"] = cart
#         request.session.modified = True

#         # Decrease product stock
#         product.product_stock -= quantity
#         product.save()

#         messages.success(request, f"Added {quantity} x {product.name} to cart.")
#         return redirect("product_list")

#     messages.error(request, "Invalid request.")
#     return redirect("product_list")
# def add_to_cart(request):
#     if request.method == 'POST':
#         cart = request.session.get('cart', {})  # Get the current cart from session
#         products = request.POST.getlist('product_ids')  # Get list of selected product IDs
#         quantities = request.POST.getlist('quantities')  # Get corresponding quantities

#         if not products or not quantities:
#             messages.error(request, "No items were selected.")
#             return redirect('product_list')

#         for product_id, quantity in zip(products, quantities):
#             try:
#                 product_id = int(product_id)
#                 quantity = int(quantity)
#                 if quantity <= 0:
#                     continue  # Skip invalid quantities

#                 product = get_object_or_404(Product, id=product_id)

#                 # Check if enough stock is available
#                 if product.product_stock < quantity:
#                     messages.warning(request, f"Not enough stock for {product.name}.")
#                     continue

#                 # Update stock in the database
#                 product.product_stock -= quantity
#                 product.save()

#                 # Add/update product in the cart session
#                 if str(product_id) in cart:
#                     cart[str(product_id)]['quantity'] += quantity
#                 else:
#                     cart[str(product_id)] = {
#                         'name': product.name,
#                         'price': product.price,
#                         'quantity': quantity,
#                     }
#             except ValueError:
#                 messages.warning(request, "Invalid product or quantity format.")
        
#         # Save updated cart in session
#         request.session['cart'] = cart
#         messages.success(request, "Cart updated successfully!")
#         return redirect('cart')  # Redirect to cart page

#     return redirect('product_list')

# def add_to_cart(request):
#     if request.method == 'POST':
#         cart = request.session.get('cart', {})  # Get the current cart from session
#         product_id = request.POST.get('product_id')  # Single product ID
#         quantity = request.POST.get('quantity')  # Quantity for the product

#         # Validate inputs
#         if not product_id or not quantity:
#             messages.error(request, "Product or quantity is missing.")
#             return redirect('product_list')

#         try:
#             product_id = int(product_id)
#             quantity = int(quantity)
#             if quantity <= 0:
#                 messages.error(request, "Quantity must be greater than zero.")
#                 return redirect('product_list')

#             # Get the product from the database
#             product = get_object_or_404(Product, id=product_id)

#             # Check if enough stock is available
#             if product.product_stock < quantity:
#                 messages.warning(request, f"Not enough stock available for {product.name}.")
#                 return redirect('product_list')

#             # Update stock in the database
#             product.product_stock -= quantity
#             product.save()

#             # Add or update the product in the cart session
#             if str(product_id) in cart:
#                 cart[str(product_id)]['quantity'] += quantity
#             else:
#                 cart[str(product_id)] = {
#                     'name': product.name,
#                     'price': product.price,
#                     'quantity': quantity,
#                 }

#             # Save the updated cart to the session
#             request.session['cart'] = cart
#             messages.success(request, f"{product.name} was added to your cart.")
#             return redirect('cart')  # Redirect to the cart page

#         except ValueError:
#             messages.error(request, "Invalid product or quantity format.")
#             return redirect('product_list')

#     return redirect('product_list')
# def add_to_cart(request):
#     if request.method == 'POST':
#         print(request.POST)
#         cart = request.session.get('cart', {})  # Get the current cart from session
#         product_id = request.POST.get('product_id')  # Single product ID from POST data
#         quantity = request.POST.get('quantity')  # Quantity for the product
        

#         # Validate inputs
#         if not product_id or not quantity:
#             messages.error(request, "Product or quantity is missing.")
#             return redirect('product_list')

#         try:
#             product_id = int(product_id)
#             quantity = int(quantity)
#             if quantity <= 0:
#                 messages.error(request, "Quantity must be greater than zero.")
#                 return redirect('product_list')

#             # Get the product from the database
#             product = get_object_or_404(Product, id=product_id)

#             # Check if enough stock is available
#             if product.product_stock < quantity:
#                 messages.warning(request, f"Not enough stock available for {product.name}.")
#                 return redirect('product_list')

#             # Update stock in the database
#             product.product_stock -= quantity
#             product.save()

#             # Add or update the product in the cart session
#             if str(product_id) in cart:
#                 cart[str(product_id)]['quantity'] += quantity
#             else:
#                 cart[str(product_id)] = {
#                     'name': product.name,
#                     'price': product.price,
#                     'quantity': quantity,
#                 }

#             # Save the updated cart to the session
#             request.session['cart'] = cart
#             messages.success(request, f"{product.name} was added to your cart.")
#             return redirect('cart')  # Redirect to the cart page

#         except ValueError:
#             messages.error(request, "Invalid product or quantity format.")
#             return redirect('product_list')

#     return redirect('product_list')
# @login_required
# def add_to_cart(request, product_id):
    
#     """
#     Add a product to the cart for logged-in users only.
#     """
#     if request.method == 'POST':
#         product_stock = int(request.POST.get('product_stock', 0))  # Get quantity from form
        
#         product = get_object_or_404(Product, id=product_id)  # Fetch the product
        

#         if product_stock > 0:
#             # Check if stock is sufficient
#             if product.product_stock < product_stock:
#                 messages.error(request, "Not enough stock available.")
#                 return redirect('product_list')

#             # Update stock
#             product.product_stock -= product_stock
#             product.save()

#             # Add to cart logic (use session for cart management)
#             cart = request.session.get('cart', {})
#             if str(product_id) in cart:
#                 cart[str(product_id)] += product_stock
#             else:
#                 cart[str(product_id)] = product_stock
#             request.session['cart'] = cart

#             messages.success(request, "Product added to cart.")
#             return redirect('cart')
#         else:
#             messages.error(request, "Invalid quantity.")
#             return redirect('product_list')
#     else:
#         return redirect('product_list')
# def add_to_cart(request, product_id):
#     # Check if the user is logged in (based on session)
#     if not request.session.get('user_id'):  # Assuming you store the logged-in user's ID in session
#         messages.error(request, "You need to log in to add items to the cart.")
#         return redirect('login')  # Redirect to login page

#     if request.method == 'POST':
#         product_stock = int(request.POST.get('product_stock', 0))  # Get quantity from form
#         product = get_object_or_404(Product, id=product_id)  # Fetch the product

#         if product_stock > 0:
#             # Check if stock is sufficient
#             if product.product_stock < product_stock:
#                 messages.error(request, "Not enough stock available.")
#                 return redirect('product_details', product_id=product_id)

#             # Update stock
#             product.product_stock -= product_stock
#             product.save()

#             # Add to cart logic (use session for cart management)
#             cart = request.session.get('cart', {})
#             if str(product_id) in cart:
#                 cart[str(product_id)]['quantity'] += product_stock
#             else:
#                 cart[str(product_id)] = {
#                     'name': product.name,
#                     'price': product.price,
#                     'quantity': product_stock,
#                 }
#             request.session['cart'] = cart

#             messages.success(request, "Product added to cart.")
#             return redirect('cart')  # Redirect to cart page
#         else:
#             messages.error(request, "Invalid quantity.")
#             return redirect('product_details', product_id=product_id)
#     else:
#         return redirect('product_list')
# def add_to_cart(request, product_id):
#     # Check if the user is logged in
#     user_id = request.session.get('user_id')  # Retrieve user ID from session
#     if not user_id:
#         messages.error(request, "You need to be logged in to add items to the cart.")
#         return redirect('login')  # Redirect to login page if not logged in

#     # Get the logged-in user
#     try:
#         user = Register.objects.get(id=user_id)
#     except Register.DoesNotExist:
#         messages.error(request, "User not found. Please log in again.")
#         return redirect('login')

#     # Process the POST request for adding an item to the cart
#     if request.method == 'POST':
#         product_stock = int(request.POST.get('product_stock', 0))  # Get the quantity
#         product = get_object_or_404(Product, id=product_id)  # Fetch the product

#         if product_stock > 0:
#             # Check if there's enough stock
#             if product.product_stock < product_stock:
#                 messages.error(request, "Not enough stock available.")
#                 return redirect('product_details', product_id=product.id)

#             # Deduct stock and save
#             product.product_stock -= product_stock
#             product.save()

#             # Manage cart in session
#             cart = request.session.get('cart', {})  # Retrieve cart from session
#             if str(product_id) in cart:
#                 cart[str(product_id)] += product_stock  # Add to existing quantity
#             else:
#                 cart[str(product_id)] = product_stock  # Add as a new product
#             request.session['cart'] = cart  # Save updated cart to session

#             messages.success(request, f"Added {product_stock} of '{product.product_name}' to your cart.")
#             return redirect('cart')  # Redirect to the cart page
#         else:
#             messages.error(request, "Invalid quantity selected.")
#             return redirect('product_details', product_id=product.id)

#     # If the request is not POST, redirect to the product list
#     return redirect('product_list')

# def product_details(request):
#    product = get_object_or_404(Product, id=product_id)
#    

#         return render(request, 'products/product_details.html', products)


#    return render(request, 'products/product_details.html',{'products':products})
# def product_details(request, product_id):
#     # Get the product using the product_id from the URL
#     product = get_object_or_404(Product, id=product_id)
#     item_name = product.name
#     # If no recommendations, set an empty list
#     if recommended_products_content.empty:
#         recommended_products_content = []

#     recommended_products_content = content_based_recommendations(item_name)

#     # Render the template with the product details
#     return render(request, 'products/product_details.html', {'product': product,'recommended_products_content': recommended_products_content})





# def product_category(request,category):
#    products = Product.objects.filter(category=category)
#    return render(request, 'products/product_category.html',{'products': products, 'category': category})


def product_category(request, sub_category_id):
    
   
    # Validate the category exists
    if not Product.objects.filter(sub_category_id=sub_category_id).exists():
        
        error_message = f"No products found in the '{sub_category_id}' category."
        return render(request, 'products/product_category.html', {'error_message': error_message})

    # Fetch products for the given category
    products = Product.objects.filter(sub_category_id=sub_category_id)

    # Pagination setup
    paginator = Paginator(products, 12)  # Show 12 products per page
    page = request.GET.get('page')

    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    # Handle search functionality
    search = request.POST.get('search')
    if search:
        search_products = Product.objects.filter(name__icontains=search)
        if not search_products.exists():
            error_message = f"No products found for '{search}'."
            return render(request, 'products/product_category.html', {'error_message': error_message})
    else:
        search_products = None
    
    # Render the template
    all_products=Product.objects.all()
    all_brands=[]

    for product in all_products:
        all_brands.append(product.name.split()[0])
    
    count_brand = Counter(all_brands)


    data = count_brand.items()
    context = {
        'data': data,
        'products': products,
        'sub_category_id': sub_category_id,
        'search_products':search_products
        }
    return render(request, 'products/product_category.html',context)

# def add_to_cart(request, product_id):
#     cart = request.session.get('cart', {})
#     quantity = int(request.POST.get('quantity', 1))

#     if product_id in cart:
#         cart[product_id] += quantity  # Increment the quantity
#     else:
#         cart[product_id] = quantity  # Add the new product

#     request.session['cart'] = cart  # Save cart to session
#     messages.success(request, 'Product added to cart.')
#     return redirect('product_list')  # Redirect to the product list or detail page




# def category_list(request):
#     all_products=Product.objects.all()
#     all_brands=set()
  

#     for product in all_products:
#         all_brands.add(product.product_name.split()[0])

#     return render(request,'products/product_list.html',{'all_brands':all_brands})

# def category_list(request):
#     all_products=Product.objects.all()
#     all_brands=[]

#     for product in all_products:
#         all_brands.append(product.product_name.split()[0])
    
#     count_brand = Counter(all_brands)


#     data = count_brand.items()
#     context = {'data': data}
#     return render(request,'products/product_list.html',context)

# def product_details(request, product_id):
#     # Get the product using the product_id from the URL
#     product = get_object_or_404(Product, id=product_id)
    
#     # Use the product's name as the item_name for content-based recommendations
#     item_name = product.name

#     # Initialize the recommended_products_content variable
#     recommended_products_content = []

#     try:
#         # Get recommended products based on content-based recommendation
#         recommended_products_content = content_based_recommendations(item_name)
#     except Exception as e:
#         # Handle any error that might occur (e.g., missing data, issues in the recommendation function)
#         print(f"Error in recommendation: {e}")

#     # If no recommendations, set an empty list
#     if recommended_products_content.empty:
#         recommended_products_content = []

#     # Render the template with the product details and recommendations
#     return render(request, 'products/product_details.html', {
#         'product': product,
#         'recommended_products_content': recommended_products_content,
#     })
# def product_details(request, product_id):
#     # Get the product using the product_id from the URL
#     product = get_object_or_404(Product, id=product_id)
    
#     # Use the product's name as the item_name for content-based recommendations
#     item_name = product.name

#     # Initialize the recommended_products_content variable
#     recommended_products_content = []

#     # Initialize a flag to indicate whether recommendations are available
#     has_recommendations = False

#     try:
#         # Get recommended products based on content-based recommendation
#         recommended_products_content = content_based_recommendations(item_name)

#         # Set flag to True if recommendations are found
#         if not recommended_products_content.empty:
#             has_recommendations = True

#     except Exception as e:
#         # Handle any error that might occur (e.g., missing data, issues in the recommendation function)
#         print(f"Error in recommendation: {e}")

#     # Render the template with the product details and recommendations
#     return render(request, 'products/product_details.html', {
#         'product': product,
#         'recommended_products_content': recommended_products_content,
#         'has_recommendations': has_recommendations,
#     })
# def product_details(request, product_id):
#     # Get the product using the product_id from the URL
#     product = get_object_or_404(Product, id=product_id)
    
#     # Use the product's name as the item_name for content-based recommendations
#     item_name = product.name

#     # Initialize the recommended_products_content variable
#     recommended_products_content = []

#     # Initialize a flag to indicate whether recommendations are available
#     has_recommendations = False

#     try:
#         # Get recommended products based on content-based recommendation
#         recommended_products_content = content_based_recommendations(item_name)

#         # Check if we get any recommendations
#         if not recommended_products_content.empty:
#             has_recommendations = True

#     except Exception as e:
#         # Handle any error that might occur (e.g., missing data, issues in the recommendation function)
#         print(f"Error in recommendation: {e}")

#     print(f"Recommended Products Content: {recommended_products_content}")  # Debugging line

#     # Render the template with the product details and recommendations
#     return render(request, 'products/product_details.html', {
#         'product': product,
#         'recommended_products_content': recommended_products_content,
#         'has_recommendations': has_recommendations,
#     })
# def product_details(request, product_id):
#     # Get the product using the product_id from the URL
#     product = get_object_or_404(Product, id=product_id)
    
#     # Use the product's name as the item_name for content-based recommendations
#     item_name = product.name

#     # Initialize the recommended_products_content variable
#     recommended_products_content = []

#     # Initialize a flag to indicate whether recommendations are available
#     has_recommendations = False

#     try:
#         # Get recommended products based on content-based recommendation
#         recommended_products_content = content_based_recommendations(item_name)

#         # Check if we get any recommendations
#         if recommended_products_content:  # Check if the list is not empty
#             has_recommendations = True

#     except Exception as e:
#         # Handle any error that might occur (e.g., missing data, issues in the recommendation function)
#         print(f"Error in recommendation: {e}")

#     print(f"Recommended Products Content: {recommended_products_content}")  # Debugging line

#     # Render the template with the product details and recommendations
#     return render(request, 'products/product_details.html', {
#         'product': product,
#         'recommended_products_content': recommended_products_content,
#         'has_recommendations': has_recommendations,
#     })
# def product_details(request, product_id):
#     # Get the product using the product_id from the URL
#     product = get_object_or_404(Product, id=product_id)
    
#     # Use the product's name as the item_name for content-based recommendations
#     item_name = product.name

#     # Initialize the recommended_products_content variable
#     recommended_products_content = []

#     # Initialize a flag to indicate whether recommendations are available
#     has_recommendations = False

#     try:
#         # Get recommended products based on content-based recommendation
#         recommended_products_content = content_based_recommendations(item_name)

#         # Check if we get any recommendations
#         if recommended_products_content:  # Check if the list is not empty
#             has_recommendations = True

#     except Exception as e:
#         # Handle any error that might occur (e.g., missing data, issues in the recommendation function)
#         print(f"Error in recommendation: {e}")

#     print(f"Recommended Products Content: {recommended_products_content}")  # Debugging line
#     print(f"Has Recommendations: {has_recommendations}")  # Debugging line

#     # Render the template with the product details and recommendations
#     return render(request, 'products/product_details.html', {
#         'product': product,
#         'recommended_products_content': recommended_products_content,
#         'has_recommendations': has_recommendations,
#     })



# def product_details(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
    
#     # Get recommended products based on the current product name
#     recommended_products = get_recommendations(product.name)

#     context = {
#         'product': product,
#         'recommended_products': recommended_products
#     }
    
#     return render(request, 'products/product_details.html', context)
# def product_details(request, product_id):
#     # Fetch the current product by ID
#     product = get_object_or_404(Product, id=product_id)
#     # Get reviews for this product
#     reviews = Review.objects.filter(product=product)
    
#     # Get recommended products based on the current product ID (not product name)
#     recommended_products = get_recommendations(product.id, top_n=12)  # Pass product.id, not product.name
#     # print(recommended_products)
#     context = {
#         'product': product,
#         'recommended_products': recommended_products
#     }
    
#     return render(request, 'products/product_details.html', context)
# def product_details(request, product_id):
#     # Fetch the current product by ID
#     product = get_object_or_404(Product, id=product_id)
    
#     # Get reviews for this product with related user data
#     reviews = Review.objects.filter(product=product).select_related('user')
    
#     # Print debug information
#     print(f"Number of reviews: {reviews.count()}")
#     for review in reviews:
#         print(f"Review by user: {review.user.name if hasattr(review.user, 'name') else 'No name'}")
    
#     # Get recommended products
#     recommended_products = get_recommendations(product.id, top_n=12)
    
#     # Handle review submission
#     if request.method == 'POST' and 'user_id' in request.session:
#         rating = request.POST.get('rating')
#         comment = request.POST.get('comment')
        
#         if rating and comment:
#             try:
#                 # Get the Register instance for the current user
#                 user = Register.objects.get(id=request.session.get('user_id'))
#                 Review.objects.create(
#                     product=product,
#                     user=user,
#                     rating=rating,
#                     comment=comment
#                 )
#                 messages.success(request, 'Your review has been submitted successfully!')
#                 return redirect('product_details', product_id=product_id)
#             except Register.DoesNotExist:
#                 messages.error(request, 'User not found.')
#             except Exception as e:
#                 messages.error(request, f'Error submitting review: {str(e)}')
    
#     context = {
#         'product': product,
#         'recommended_products': recommended_products,
#         'reviews': reviews,
#         'review_count': reviews.count()
#     }
    
#     # Debug print
#     print(f"Context reviews count: {context['review_count']}")
    
#     return render(request, 'products/product_details.html', context)

# def product_details(request, product_id):
#     # Fetch the current product by ID
#     product = get_object_or_404(Product, id=product_id)
    
#     # Get reviews for this product with related user data
#     reviews = Review.objects.filter(product=product).select_related('user')
    
#     # Handle review submission
#     if request.method == 'POST' and 'user_id' in request.session:
#         rating = request.POST.get('rating')
#         comment = request.POST.get('comment')
        
#         if rating and comment:
#             try:
#                 # Get the Register instance for the current user
#                 user = Register.objects.get(id=request.session.get('user_id'))
#                 Review.objects.create(
#                     product=product,
#                     user=user,
#                     rating=rating,
#                     comment=comment
#                 )
#                 messages.success(request, 'Your review has been submitted successfully!')
#                 return redirect('product_details', product_id=product_id)
#             except Register.DoesNotExist:
#                 messages.error(request, 'User not found.')
#             except Exception as e:
#                 messages.error(request, f'Error submitting review: {str(e)}')
    
#     # Get recommended products
#     recommended_products = get_recommendations(product.id, top_n=12)
    
#     context = {
#         'product': product,
#         'recommended_products': recommended_products,
#         'reviews': reviews,
#         'review_count': reviews.count()
#     }
    
#     return render(request, 'products/product_details.html', context)

# def product_details(request, product_id):
#     print("Method:", request.method)
#     print("Session:", request.session.items())
#     # Fetch the current product by ID
#     product = get_object_or_404(Product, id=product_id)
    
#     # Get reviews for this product with related user data
#     reviews = Review.objects.filter(product=product).select_related('user')
    
#     # Handle review submission
#     if request.method == 'POST' and 'user_id' in request.session:
#         print("POST data:", request.POST)
#         print("User ID in session:", request.session.get('user_id'))
#         rating = request.POST.get('rating')
#         comment = request.POST.get('comment')
        
#         if rating and comment:
#             try:
#                 # Get the Register instance for the current user
#                 user = Register.objects.get(id=request.session.get('user_id'))
#                 Review.objects.create(
#                     product=product,
#                     user=user,
#                     rating=rating,
#                     comment=comment
#                 )
#                 messages.success(request, 'Your review has been submitted successfully!')
#                 return redirect('product_details', product_id=product_id)
#             except Register.DoesNotExist:
#                 messages.error(request, 'User not found.')
#             except Exception as e:
#                 messages.error(request, f'Error submitting review: {str(e)}')
    
#     # Get recommended products
#     recommended_products = get_recommendations(product.id, top_n=12)
    
#     context = {
#         'product': product,
#         'recommended_products': recommended_products,
#         'reviews': reviews,
#         'review_count': reviews.count()
#     }
    
#     return render(request, 'products/product_details.html', context)

def product_details(request, product_id):
    # print("Method:", request.method)
    # print("Session:", request.session.items())
    # Fetch the current product by ID
    product = get_object_or_404(Product, id=product_id)
    
    # Get reviews for this product with related user data
    reviews = Review.objects.filter(product=product).select_related('user')
    
    # Handle review submission
    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        
        if rating and comment:
            try:
                # Get the Register instance for the current user
                user = Register.objects.get(id=request.user.id)
                Review.objects.create(
                    product=product,
                    user=user,
                    rating=rating,
                    comment=comment
                )
                messages.success(request, 'Your review has been submitted successfully!')
                return redirect('product_details', product_id=product_id)
            except Register.DoesNotExist:
                messages.error(request, 'User not found.')
            except Exception as e:
                messages.error(request, f'Error submitting review: {str(e)}')
                # print(f"Error creating review: {e}")  # Debug print
    
    # Get recommended products
    recommended_products = get_recommendations(product.id, top_n=12)
    
    context = {
        'product': product,
        'recommended_products': recommended_products,
        'reviews': reviews,
        'review_count': reviews.count()
    }
    
    return render(request, 'products/product_details.html', context)







