from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from apps.admin1.models import Product
from django.db.models import F
from .models import Cart,CartItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import razorpay

# Create your views here.
# def cart(request):
#     return render(request, 'cart/cart.html')
# def cart(request):
#     # Retrieve the cart from the session, or initialize an empty cart if it doesn't exist
#     cart = request.session.get('cart', {})

#     cart_items = []
#     total_price = 0

#     for product_id, quantity in cart.items():
#         try:
#             product = Product.objects.get(id=product_id)
#             total_price += product.product_price * quantity
#             cart_items.append({
#                 'product': product,
#                 'quantity': quantity,
#                 'subtotal': product.product_price * quantity
#             })
#         except Product.DoesNotExist:
#             # If the product no longer exists, remove it from the cart
#             continue

#     if request.method == 'POST':
#         # Handle removing an item from the cart
#         product_id = request.POST.get('product_id')
#         if product_id in cart:
#             quantity = cart[product_id]  # Get the quantity to restore stock
#             try:
#                 product = Product.objects.get(id=product_id)
#                 product.product_stock += quantity  # Increase stock
#                 product.save()  # Save the updated stock
#             except Product.DoesNotExist:
#                 messages.error(request, "Product not found.")

#             del cart[product_id]  # Remove the item from the cart
#             request.session['cart'] = cart  # Update the session
#             messages.success(request, 'Item removed from cart.')

#         return redirect('my_cart')  # Reload the cart page

#     context = {
#         'cart_items': cart_items,
#         'total_price': total_price
#     }
#     return render(request, 'cart/cart.html', context)
# def cart(request):
#     # Retrieve the cart from the session, or initialize an empty cart if it doesn't exist
#     cart = request.session.get('cart', {})
#     cart_items = []
#     total_price = 0

#     # Fetch all products in the cart in a single query
#     product_ids = cart.keys()
#     products = Product.objects.filter(id__in=product_ids)

#     for product in products:
#         quantity = cart.get(str(product.id), 0)  # Quantity from the cart
#         subtotal = product.product_price * quantity  # Calculate subtotal
#         total_price += subtotal  # Add to total price
#         cart_items.append({
#             'product': product,
#             'quantity': quantity,
#             'subtotal': subtotal,
#         })

#     if request.method == 'POST':
#         # Handle removing an item from the cart
#         product_id = request.POST.get('product_id')
#         if product_id and product_id in cart:
#             try:
#                 product = Product.objects.get(id=product_id)
#                 quantity = cart[product_id]  # Get the quantity to restore stock
#                 product.product_stock += quantity  # Restore stock
#                 product.save()  # Save the updated stock

#                 # Remove the item from the cart
#                 del cart[product_id]
#                 request.session['cart'] = cart  # Update session

#                 messages.success(request, 'Item removed from cart.')
#             except Product.DoesNotExist:
#                 messages.error(request, "Product not found.")
#             return redirect('cart')  # Reload the cart page

#     context = {
#         'cart_items': cart_items,
#         'total_price': total_price,
#     }
#     return render(request, 'cart/cart.html', context)
# Cart view
# def cart(request):
#     cart = request.session.get('cart', {})
#     cart_items = []
#     total_price = 0

#     for product_id, quantity in cart.items():
#         product = get_object_or_404(Product, id=product_id)
#         subtotal = product.discount_price * quantity
#         total_price += subtotal
#         cart_items.append({
#             'product': product,
#             'quantity': quantity,
#             'subtotal': subtotal,
#         })

#     context = {
#         'cart_items': cart_items,
#         'total_price': total_price,
#     }
#     return render(request, 'cart/cart.html', context)
# # Update cart view
# def update_cart(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         new_quantity = int(request.POST.get('new_quantity', 0))

#         cart = request.session.get('cart', {})

#         if product_id in cart:
#             product = get_object_or_404(Product, id=product_id)
#             if new_quantity <= 0:
#                 # Remove item from cart
#                 del cart[product_id]
#                 messages.success(request, f"{product.name} removed from the cart.")
#             elif product.product_stock + cart[product_id] < new_quantity:
#                 messages.error(request, f"Only {product.product_stock + cart[product_id]} items available.")
#             else:
#                 # Update cart quantity and restore stock difference
#                 stock_difference = new_quantity - cart[product_id]
#                 product.product_stock = F('product_stock') - stock_difference
#                 product.save()
#                 cart[product_id] = new_quantity
#                 messages.success(request, f"{product.name} quantity updated to {new_quantity}.")
#             request.session['cart'] = cart

#         return redirect('cart')
# def add_to_cart(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')  # Get product ID from the form
#         quantity = int(request.POST.get('quantity', 1))  # Default quantity to 1

#         # Validate that product_id is a number
#         if not product_id.isdigit():
#             messages.error(request, "Invalid product ID.")
#             return redirect('product_list')  # Redirect to product list page

#         product_id = int(product_id)

#         # Get the current cart from session or initialize an empty cart
#         cart = request.session.get('cart', {})

#         # Update the cart: Add the quantity to the existing product or set it
#         cart[product_id] = cart.get(product_id, 0) + quantity

#         # Save the updated cart in the session
#         request.session['cart'] = cart
#         request.session.modified = True  # Mark session as modified

#         messages.success(request, "Product added to cart!")
#         return redirect('product_list')  # Redirect to product list page


# @login_required
# def cart(request):
#     try:
#         # Get or create the user's cart
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         cart_items = cart.items.all()
#         total_price = 0

#         for item in cart_items:
#             subtotal = item.product.discount_price * item.quantity
#             total_price += subtotal

#         context = {
#             'cart_items': cart_items,
#             'total_price': total_price,
#         }
#         return render(request, 'cart/cart.html', context)
#     except Cart.DoesNotExist:
#         return render(request, 'cart/cart.html', {'cart_items': [], 'total_price': 0})
# @login_required
# def cart(request):
#     try:
#         # Get or create the user's cart
#         cart, created = Cart.objects.get_or_create(user=request.user)
#         cart_items = cart.items.all()
#         total_price = 0
#         cart_item_details = []

#         for item in cart_items:
#             # Calculate the subtotal for each item
#             subtotal = item.product.discount_price * item.quantity
#             total_price += subtotal
#             cart_item_details.append({
#                 'item': item,
#                 'subtotal': subtotal
#             })

#         context = {
#             'cart_items': cart_item_details,  # Pass the cart items along with subtotal
#             'total_price': total_price,
#         }
#         return render(request, 'cart/cart.html', context)
#     except Cart.DoesNotExist:
#         return render(request, 'cart/cart.html', {'cart_items': [], 'total_price': 0})
# @login_required
# def cart(request):
#     try:
#         # Check if the user is authenticated
#         if request.user.is_authenticated:
#             # Get or create the user's cart
#             cart, created = Cart.objects.get_or_create(user=request.user)
            
            
#             # Check if cart was created (for debugging purposes)
#             if created:
#                 print(f"Cart created for user: {request.user.username}")
#             else:
#                 print(f"Cart already exists for user: {request.user.username}")
            
#             cart_items = cart.items.all()
#             total_price = 0
#             cart_item_details = []

#             for item in cart_items:
#                 # Calculate the subtotal for each item
#                 subtotal = item.product.discount_price * item.quantity
#                 total_price += subtotal
#                 cart_item_details.append({
#                     'item': item,
#                     'subtotal': subtotal
#                 })

#             context = {
#                 'cart_items': cart_item_details,  # Pass the cart items along with subtotal
#                 'total_price': total_price,
#             }
#             return render(request, 'cart/cart.html', context)
        
#         else:
#             return redirect('login')  # Redirect to login page if user is not authenticated
        
#     except Cart.DoesNotExist:
#         return render(request, 'cart/cart.html', {'cart_items': [], 'total_price': 0})
@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()

    cart_item_details = [
        {'item': item, 'subtotal': item.product.discount_price * item.quantity}
        for item in cart_items
    ]
    total_price = sum(item['subtotal'] for item in cart_item_details)

    return render(request, 'cart/cart.html', {
        'cart_items': cart_item_details,
        'total_price': total_price
    })


# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     quantity = int(request.POST.get('quantity', 1))

#     # Get the user's cart or create a new one if it doesn't exist
#     cart, created = Cart.objects.get_or_create(user=request.user)

#     # Check if the product is already in the cart
#     cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

#     if item_created:
#         cart_item.quantity = quantity
#         messages.success(request, f'{product.name} added to cart.')
#     else:
#         cart_item.quantity += quantity
#         messages.success(request, f'{product.name} quantity updated in cart.')

#     cart_item.save()
#     return redirect('product_list')  # Redirect to product list or product details
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     quantity = int(request.POST.get('quantity', 1))

#     # Get the user model dynamically (this will handle custom user models like 'Register')
#     User = get_user_model()

#     # Ensure that the user is authenticated
#     if not request.user.is_authenticated:
#         messages.error(request, 'You must be logged in to add items to your cart.')
#         return redirect('login')  # Redirect to your login page

#     # Get or create the user's cart
#     cart, created = Cart.objects.get_or_create(user=request.user)

#     # Check if the product is already in the cart
#     cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

#     if item_created:
#         cart_item.quantity = quantity
#         messages.success(request, f'{product.name} added to cart.')
#     else:
#         cart_item.quantity += quantity
#         messages.success(request, f'{product.name} quantity updated in cart.')

#     cart_item.save()
#     return redirect('product_list')  # Redirect to product list or product details
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)

#     if request.method == 'POST':
    
#      # Get the quantity from the POST request, defaulting to 1 if not provided
#      quantity = request.POST.get('quantity', 1)
    
#     # Ensure the quantity is a valid integer
#     try:
#         quantity = int(quantity)
#         if quantity < 1:
#             quantity = 1  # Enforce a minimum of 1
#     except ValueError:
#         quantity = 1  # Default to 1 if the conversion fails

#     # Get the user model dynamically (this will handle custom user models like 'Register')
#     User = get_user_model()

#     # Ensure that the user is authenticated
#     if not request.user.is_authenticated:
#         messages.error(request, 'You must be logged in to add items to your cart.')
#         return redirect('login')  # Redirect to your login page

#     # Get or create the user's cart
#     cart, created = Cart.objects.get_or_create(user=request.user)

#     # Check if the product is already in the cart
#     cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

#     # Ensure the quantity is always set before saving
#     cart_item.quantity = quantity

#     if item_created:
#         messages.success(request, f'{product.name} added to cart.')
#     else:
#         messages.success(request, f'{product.name} quantity updated in cart.')

#     cart_item.save()
#     return redirect('product_list')  # Redirect to product list or product details
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
    
#     # Get the quantity from the POST request, defaulting to 1 if not provided
#     quantity_str = request.POST.get('quantity', '1')
    
#     # Ensure the quantity is a valid integer
#     try:
#         quantity = int(quantity_str)
#         if quantity < 1:
#             quantity = 1  # Enforce a minimum of 1
#     except ValueError:
#         quantity = 1  # Default to 1 if the conversion fails

#     # Ensure the user is authenticated
#     if not request.user.is_authenticated:
#         messages.error(request, 'You must be logged in to add items to your cart.')
#         return redirect('login')  # Redirect to login page

#     # Get or create the user's cart
#     cart, created = Cart.objects.get_or_create(user=request.user)

#     # Try to get the existing CartItem, or create a new one if it doesn't exist
#     cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

#     if item_created:
#         # If the CartItem was created, set the quantity
#         cart_item.quantity = quantity
#         messages.success(request, f'{product.name} added to cart.')
#     else:
#         # If the CartItem already exists, update the quantity
#         cart_item.quantity += quantity
#         messages.success(request, f'{product.name} quantity updated in cart.')

#     # Save the CartItem with the updated quantity
#     cart_item.save()
    
#     return redirect('product_list')  # Redirect to the product list or product details
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
    
#     # Get the quantity from the POST request, defaulting to 1 if not provided
#     quantity_str = request.POST.get('quantity', '1')
    
#     # Ensure the quantity is a valid integer
#     try:
#         quantity = int(quantity_str)
#         if quantity < 1:
#             quantity = 1  # Enforce a minimum of 1
#     except ValueError:
#         quantity = 1  # Default to 1 if the conversion fails

#     # Ensure the user is authenticated
#     if not request.user.is_authenticated:
#         messages.error(request, 'You must be logged in to add items to your cart.')
#         return redirect('login')  # Redirect to login page

#     # Get or create the user's cart
#     cart, created = Cart.objects.get_or_create(user=request.user)

#     # Try to get the existing CartItem, or create a new one with the specified quantity
#     cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': quantity})

#     if item_created:
#         messages.success(request, f'{product.name} added to cart.')
#     else:
#         # If the CartItem already exists, update the quantity
#         cart_item.quantity += quantity
#         messages.success(request, f'{product.name} quantity updated in cart.')

#     # Save the CartItem with the updated quantity
#     cart_item.save()
    
#     return redirect('product_list')  # Redirect to the product list or product details
# @login_required
# def add_to_cart(request, product_id):
#     try:
#         # Get the product from the product_id
#         product = Product.objects.get(id=product_id)
        
#         # Get or create the user's cart
#         cart, created = Cart.objects.get_or_create(user=request.user)

#         # Check if the item already exists in the cart, and update quantity or create a new entry
#         cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
        
#         if not item_created:
#             # If the item already exists, increment the quantity
#             cart_item.quantity += 1
#             cart_item.save()
#         else:
#             cart_item.quantity = 1  # Set initial quantity to 1 if newly added
        
#         messages.success(request, f'{product.name} has been added to your cart.')
#         return redirect('cart')  # Redirect to the cart page

#     except Product.DoesNotExist:
#         messages.error(request, 'Product not found.')
#         return redirect('product_list')  # Redirect to the homepage or product list
# @login_required
# def add_to_cart(request, product_id):
#     if request.method == "POST":
#         product = get_object_or_404(Product, id=product_id)
#         cart, created = Cart.objects.get_or_create(user=request.user)

#          # Get the quantity from the POST request, defaulting to 1 if not provided
#         quantity = request.POST.get('quantity',1)
    
#         # Ensure the quantity is a valid integer
#         try:
#           quantity = int(quantity)
#           if quantity < 1:
#               quantity = 1  # Enforce a minimum of 1
#         except ValueError:
#             quantity = 1  # Default to 1 if the conversion fails
        
#         # Add the product to the cart (or update quantity)
#         cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
#         cart_item.quantity += 1
#         cart_item.save()
        
#         messages.success(request, f"{product.name} has been added to your cart.")
#         return redirect('cart')  # Redirect to the cart page

#     return redirect('products')  # Redirect to product list if not POST
# @login_required
# def add_to_cart(request, product_id):
#     if request.method == "POST":
#         product = get_object_or_404(Product, id=product_id)
#         cart, created = Cart.objects.get_or_create(user=request.user)

#         # Get the quantity from the POST request, defaulting to 1 if not provided
#         quantity = request.POST.get('quantity', 1)

#         # Ensure the quantity is a valid integer
#         try:
#             quantity = int(quantity)
#             if quantity < 1:
#                 quantity = 1  # Enforce a minimum of 1
#         except ValueError:
#             quantity = 1  # Default to 1 if the conversion fails

#         # Add the product to the cart (or update quantity)
#         cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
#         cart_item.quantity += quantity  # Increment by the specified quantity
#         cart_item.save()

#         messages.success(request, f"{product.name} has been added to your cart.")
#         return redirect('cart')  # Redirect to the cart page

#     return redirect('products')  # Redirect to product list if not POST
@login_required
def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Get the quantity from the POST request, defaulting to 1 if not provided
        quantity = request.POST.get('quantity', 1)

        # Ensure the quantity is a valid integer
        try:
            quantity = int(quantity)
            if quantity < 1:
                quantity = 1  # Enforce a minimum of 1
        except ValueError:
            quantity = 1  # Default to 1 if the conversion fails

        # Add the product to the cart (or update quantity)
        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart, 
            product=product,
            defaults={'quantity': 0}  # Provide a default value for quantity
        )
        cart_item.quantity += quantity  # Increment the quantity
        cart_item.save()

        messages.success(request, f"{product.name} has been added to your cart.")
        return redirect('product_list')

    return redirect('products_list')  # Redirect to product list if not POST

def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        new_quantity = int(request.POST.get('new_quantity', 0))

        cart = Cart.objects.get(user=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)

        if new_quantity <= 0:
            cart_item.delete()
            messages.success(request, f"{cart_item.product.name} removed from the cart.")
        elif new_quantity > cart_item.product.product_stock:
            messages.error(request, f"Only {cart_item.product.product_stock} items available.")
        else:
            cart_item.quantity = new_quantity
            cart_item.save()
            messages.success(request, f"{cart_item.product.name} quantity updated to {new_quantity}.")

        return redirect('cart')