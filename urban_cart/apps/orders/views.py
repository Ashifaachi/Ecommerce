from django.shortcuts import render,redirect
from apps.payments.models import Order,OrderItem
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def order(request):
    """Display a list of all orders for the logged-in user."""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')  # Fetch orders for logged-in user
    return render(request, 'orders/order_history.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    """Display details of a specific order."""
    order = get_object_or_404(Order, id=order_id, user=request.user)  # Ensure user can only view their own orders

    order_items = []
    for item in order.items.all():
        item.subtotal = item.quantity * item.price
        order_items.append(item)
    return render(request, 'orders/order_detail.html', {'order': order,'order_items': order_items,})


@login_required
def mark_order_complete(request, order_id):
    """Manually mark an order as completed."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status != "Completed":
        order.status = "Completed"
        order.save()
    return redirect('orders', )


def razorpay_payment_success(request, order_id):
    """Handle successful Razorpay payments and mark the order as completed."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Capture Razorpay payment details
    order.razorpay_payment_id = request.GET.get("razorpay_payment_id")
    order.razorpay_order_id = request.GET.get("razorpay_order_id")
    order.razorpay_signature = request.GET.get("razorpay_signature")
    
    # ✅ Automatically mark the order as 'Completed'
    order.status = "Completed"
    order.save()
    
    return redirect('order_detail', order_id=order.id)  # Redirect to order details page