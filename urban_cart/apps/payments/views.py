from pyexpat.errors import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import Address
from django.contrib.auth.decorators import login_required
from apps.users.models import State, District
import razorpay
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, OrderItem
from apps.cart.models import Cart, CartItem
# Create your views here.
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
# def checkout(request):
#     if not request.user.is_authenticated:
#         return redirect('users:login')

#     cart = Cart.objects.get(user=request.user)
#     cart_items = CartItem.objects.filter(cart=cart)

#     total_amount = sum(item.product.discount_price * item.quantity for item in cart_items)

#     # Create Razorpay order
#     order_data = {
#         'amount': int(total_amount * 100),  # Convert to paise
#         'currency': 'INR',
#         'payment_capture': '1'  # Auto capture
#     }
#     razorpay_order = razorpay_client.order.create(order_data)
    

#     # Save order and payment details
#     payment = Payment.objects.create(
#         user=request.user,
#         razorpay_order_id=razorpay_order['id'],
#         amount=total_amount,
#         status='Pending'
#     )
    
#     order = Order.objects.create(user=request.user, payment=payment)

#     for item in cart_items:
#         OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.discount_price)

#     cart_items.delete()  # Clear cart after order is placed

#     context = {
#         'order': order,
#         'payment': payment,
#         'razorpay_key': settings.RAZORPAY_KEY_ID
#     }
#     return render(request, 'payments/checkout.html', context)
# @login_required
# def checkout(request):
#     cart = Cart.objects.get(user=request.user)
#     cart_items = cart.items.all()
#     total_price = sum(item.product.discount_price * item.quantity for item in cart_items)
    
#     address = Address.objects.filter(user=request.user).last()
#     if not address:
#         return redirect('add_address')

#     client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#     razorpay_order = client.order.create({
#         "amount": int(total_price * 100),
#         "currency": "INR",
#         "payment_capture": "1"
#     })

#     order = Order.objects.create(
#         user=request.user,
#         address=address,
#         total_price=total_price,
#         razorpay_order_id=razorpay_order['id']
#     )

#     for item in cart_items:
#         OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.discount_price)
    
#     context = {
#         "cart_items": cart_items,
#         "total_price": total_price,
#         "order": order,
#         "razorpay_order_id": razorpay_order['id'],
#         "razorpay_key": settings.RAZORPAY_KEY_ID
#     }
#     return render(request, "payments/checkout.html", context)
@login_required
def checkout(request):
    # First check if user has an address
    user_has_address = Address.objects.filter(user=request.user).exists()
    if not user_has_address:
        return redirect('add_address')
    
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()
    if not cart_items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('cart')

    total_price = sum(item.product.discount_price * item.quantity for item in cart_items)
    

    address = Address.objects.filter(user=request.user).last()
    

    # Create Razorpay order
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    razorpay_order = client.order.create({
        "amount": int(total_price * 100),  # Razorpay expects the amount in paise (1 INR = 100 paise)
        "currency": "INR",
        "payment_capture": "1"
    })

    # Create the Order
    order = Order.objects.create(
        user=request.user,
        address=address,
        total_price=total_price,
        razorpay_order_id=razorpay_order['id']
    )

    # Process each cart item
    for item in cart_items:
        # Create the OrderItem for the order
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.discount_price
        )

        # Reduce the product stock
        product = item.product
        if product.product_stock >= item.quantity:
            product.product_stock -= item.quantity
            product.save()  # Save the updated product stock
        
        # Remove the CartItem
        item.delete()

    # Clear the cart after processing
    cart.delete()

    # Prepare context for rendering the checkout page
    context = {
        "cart_items": cart_items,
        "total_price": total_price,
        "order": order,
        "razorpay_order_id": razorpay_order['id'],
        "razorpay_key": settings.RAZORPAY_KEY_ID
    }
    
    return render(request, "payments/checkout.html", context)
def payment_status(request):
    return render(request, 'pyments/payment_status.html')
def payment_success(request):
    return render(request, "payments/payment_success.html")

def payment_cancel(request):
    return render(request, "payments/payment_cancel.html")

# @login_required
# def add_address(request):
#     if request.method == "POST":
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         address = request.POST.get("address")
#         address2 = request.POST.get("address2")
#         state_id = request.POST.get("state")
#         district_id = request.POST.get("district")
#         pin = request.POST.get("pin")

#         if not all([first_name, last_name, email, phone, address, state_id, district_id, pin]):
#             return render(request, "payments/add_address.html", {"error": "All fields are required."})

#         state = State.objects.get(id=state_id)
#         district = District.objects.get(id=district_id)

#         Address.objects.create(
#             user=request.user,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             phone=phone,
#             address=address,
#             address2=address2,
#             state=state,
#             district=district,
#             pin=pin,
#         )

#         return redirect("checkout")

#     states = State.objects.all()
#     districts = District.objects.all()
#     address = Address.objects.all()
#     return render(request, "payments/add_address.html", {"states": states,'districts':districts,'address':address})
# @login_required
# def add_address(request):
#     if request.method == "POST":
#         # Extracting POST data
#         first_name = request.POST.get("first_name")
#         last_name = request.POST.get("last_name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         address = request.POST.get("address")
#         address2 = request.POST.get("address2")
#         state_id = request.POST.get("state")
#         district_id = request.POST.get("district")
#         pin = request.POST.get("pin")

#         # Check if all required fields are filled
#         if not all([first_name, last_name, email, phone, address, state_id, district_id, pin]):
#             return render(request, "payments/add_address.html", {"error": "All fields are required."})

#         # Get state and district instances
#         state = State.objects.get(id=state_id)
#         district = District.objects.get(id=district_id)

#         # Create address object
#         Address.objects.create(
#             user=request.user,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             phone=phone,
#             address=address,
#             address2=address2,
#             state=state,
#             district=district,
#             pin=pin,
#         )

#         # Redirect to checkout if address is added successfully
#         return redirect("checkout")

#     # Pass states and districts to the template
#     states = State.objects.all()
#     districts = District.objects.all()

#     return render(request, "payments/add_address.html", {"states": states, "districts": districts})
@login_required
def get_districts(request, state_id):
    try:
        # Add print statements for debugging
        print(f"Fetching districts for state_id: {state_id}")
        
        districts = District.objects.filter(state_id=state_id)
        print(f"Found {districts.count()} districts")
        
        district_list = [{'id': district.id, 'name': district.name} 
                        for district in districts]
        
        print(f"District list: {district_list}")
        
        return JsonResponse(district_list, safe=False)
    except Exception as e:
        print(f"Error in get_districts: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

@login_required
def add_address(request):
    # Check if the user already has an address
    if request.user.address_set.exists():
        # Redirect to checkout if an address exists
        return redirect("checkout")
    states = State.objects.all().order_by('name')

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        address2 = request.POST.get("address2")
        state_id = request.POST.get("state")
        district_id = request.POST.get("district")
        pin = request.POST.get("pin")

        # Validate all fields
        if not all([first_name, last_name, email, phone, address, state_id, district_id, pin]):
            return render(request, "payments/add_address.html", {"error": "All fields are required."})

        try:
            # Fetch state and district
            state = State.objects.get(id=state_id)
            district = District.objects.get(id=district_id)
            
            # Create the address
            Address.objects.create(
                user=request.user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                address2=address2,
                state=state,
                district=district,
                pin=pin,
            )
            messages.success(request, "Address added successfully!")
            return redirect("checkout")  # Redirect to checkout after saving the address

        except (State.DoesNotExist, District.DoesNotExist):
            messages.error(request, "Invalid state or district selected.")
            return render(request, "payments/add_address.html", {
                "states": State.objects.all(),
                "districts": District.objects.all(),
                "error": "Invalid state or district selected."
            })
        
    context = {
        'states': states,
        'districts': District.objects.none()  # Empty queryset for initial load
    }
        
    

    # Fetch states and districts for the form
    
    return render(request, "payments/add_address.html", context)
# def get_districts(request, state_id):
#     try:
#         districts = District.objects.filter(state_id=state_id).values('id', 'name')
#         return JsonResponse(list(districts), safe=False)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)
# @login_required
# def payment_success(request):
#     payment_id = request.GET.get('payment_id')
#     if request.method == "POST":
#         razorpay_payment_id = request.POST.get("razorpay_payment_id")
#         razorpay_order_id = request.POST.get("razorpay_order_id")
#         razorpay_signature = request.POST.get("razorpay_signature")

#         order = Order.objects.get(razorpay_order_id=razorpay_order_id)
#         order.razorpay_payment_id = razorpay_payment_id
#         order.razorpay_signature = razorpay_signature
#         order.status = "Completed"
#         order.save()

#         return JsonResponse({"success": True,})

#     return JsonResponse({"error": "Invalid request"}, status=400)
# def payment_success(request):
#     payment_id = request.GET.get('payment_id')
#     # You can also include more logic to process the payment success here

#     return render(request, 'payments/success.html', {'payment_id': payment_id})
@login_required
def payment_success(request):
    payment_id = request.GET.get('payment_id')
    
    # Step 1: Get the user's cart and cart items
    cart = Cart.objects.filter(user=request.user, is_ordered=False).first()  # Assuming 'is_ordered' is used to mark an unprocessed cart
    if cart:
        cart_items = CartItem.objects.filter(cart=cart)
        
        # Step 2: Update product stock and clear cart items
        for item in cart_items:
            product = item.product
            if product.product_stock >= item.quantity:
                # Decrease the stock based on the quantity of the product in the cart
                product.product_stock -= item.quantity
                product.save()

        # Step 3: Clear the cart by deleting the cart items
        cart_items.delete()

        # Step 4: Optionally, mark the cart as 'ordered' or similar to indicate it's processed
        cart.is_ordered = True
        cart.save()

        # Redirect to the success page
        return render(request, 'payments/success.html', {'payment_id': payment_id})
    
    # If cart not found, return an error page or redirect
    return redirect('cart')
def payment_failed(request):
    return render(request, 'payments/payment_failed.html')






def get_districts(request, state_id):
    districts = District.objects.filter(state_id=state_id).values("id", "name")
    return JsonResponse(list(districts), safe=False)