from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .models import Product,Slider,MainCategory,SubCategory,Manufacturer
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django import template

register = template.Library()

@register.filter
def divide_into(items, n):
    """Divide a list into sublists of size n"""
    return [items[i:i + n] for i in range(0, len(items), n)]

# Create your views here.
def index(request):
    return render(request, 'admin1/admin_dashboard.html')
def add_item(request):
     context = {
        'main_category': MainCategory.objects.all(),
        'sub_category': SubCategory.objects.all(),
        'manufacturer':Manufacturer.objects.all(),
    }
     
     if request.method == 'POST':
        name = request.POST.get('name')
        manufacturer = request.POST.get('manufacturer')
        manufacturer = get_object_or_404(Manufacturer, name=manufacturer)
        main_category = request.POST.get('main_category')
        main_category = get_object_or_404(MainCategory, name=main_category)
        sub_category = request.POST.get('sub_category')
        sub_category = get_object_or_404(SubCategory, name=sub_category)
        image_url = request.POST.get('image_url')
        site_link = request.POST.get('site_link')
        ratings = float(request.POST.get('ratings', '0') or 0.0)
        no_of_ratings = int(request.POST.get('no_of_ratings', '0') or 0)
        discount_price = float(request.POST.get('discount_price', '0') or 0.0)
        actual_price = float(request.POST.get('actual_price', '0') or 0.0)
        product_stock = int(request.POST.get('product_stock', '0') or 0)
        product, created = Product.objects.get_or_create(
            name=name,
            defaults={
                'manufacturer':manufacturer,
                'main_category': main_category,
                'sub_category': sub_category,
                'image_url': image_url,
                'site_link': site_link,
                'ratings': ratings,
                'no_of_ratings':no_of_ratings,
                'product_stock': product_stock,
                'discount_price': discount_price,
                'actual_price':actual_price
            }
        )

        if not created:
            # If Product exists, update its quantity
            product.product_stock += product_stock
            product.save()
        else:
            # If newly created, save it now
            product.save()
       

        return redirect('add_item')

     return render(request, 'admin1/add_item.html',context)



    #return render(request, 'admin1/add_item.html')
# def delete_item(request):
#      if request.method == 'POST':
#         product_name = request.POST.get('product_name')

#         # Find the book with the specified name
#         product = Product.objects.filter(product_name=product_name)

#         if product.exists():
#             product.delete()  # Deletes the matching product(s)
#             message = f"product '{product_name}' deleted successfully."
#         else:
#             message = f"product '{product_name}' not found."

#         return render(request, 'admin1/delete_item.html', {'message': message})
#      return render(request, 'admin1/delete_item.html')
# def delete_item(request):
#     # Autocomplete functionality
#     if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))
#         titles = [product.name for product in qs][:10]
#         return JsonResponse(titles, safe=False)

#     search_products = None
#     product = None  # Initialize product to None

#     if request.method == 'POST':
#         name = request.POST.get('name')

#         # Find the product with the specified name
#         product = Product.objects.filter(name=name)

#         if product.exists():
#             product.delete()  # Deletes the matching product(s)
#             message = f"Product '{name}' deleted successfully."
#         else:
#             message = f"Product '{name}' not found."

#         return render(request, 'admin1/delete_item.html', {'message': message,'search_products':search_products})

#     return render(request, 'admin1/delete_item.html', { 'search_products':search_products})  # Default message for GET
     
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# def delete_item(request):
#     # Autocomplete functionality
#     if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))
#         titles = [product.name for product in qs][:10]
#         return JsonResponse(titles, safe=False)

#     context = {
#         'search_products': None,
#         'message': None
#     }

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         confirm = request.POST.get('confirm', 'false')

#         if not name:
#             messages.error(request, "Product name is required.")
#             return render(request, 'admin1/delete_item.html', context)

#         try:
#             # Use get() instead of filter() to ensure only one product is deleted
#             product = Product.objects.get(name=name)
            
#             # Check for confirmation
#             if confirm == 'true':
#                 product.delete()
#                 messages.success(request, f"Product '{name}' deleted successfully.")
#             else:
#                 # If not confirmed, show confirmation page
#                 context['product'] = product
#                 context['confirm'] = True
#                 return render(request, 'admin1/delete_item.html', context)

#         except ObjectDoesNotExist:
#             messages.error(request, f"Product '{name}' not found.")
#         except Exception as e:
#             messages.error(request, f"Error deleting product: {str(e)}")

#     return render(request, 'admin1/delete_item.html', context)    
# def update_item(request):
#       # ✅ Autocomplete functionality
#     if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     product = None  # Initialize product variable
#     search_products = None
#     error_message = None
#     success_message = None

#     # ✅ Search functionality
#     search = request.POST.get('search_name')
#     if search:
#         search_products = Product.objects.filter(name__icontains=search)
#         if not search_products.exists():
#             error_message = f"No products found for '{search}'."
#             return render(request, 'admin1/update_item.html', {'error_message': error_message})
        

#     if request.method == 'POST':
#         search_name = request.POST.get('product_name')

#         # Try to find the book using search_name
#         product = get_object_or_404(Product, product_name=search_name)

#         # Update the book's attributes if found
#         if 'product_name' in request.POST:
#             product.product_name = request.POST.get('product_name', product.product_name)
#         if 'product_category' in request.POST:
#             product.product_category = request.POST.get('product_category', product.product_category)
#         if 'product_description' in request.POST:
#             product.product_description = request.POST.get('product_description', product.product_description)
#         if 'product_stock' in request.POST:
#             product.product_stock = int(request.POST.get('product_stock', product.product_stock))
#         if 'product_price' in request.POST:
#             product.product_price = float(request.POST.get('product_price', product.product_price))
#         if 'product_image1' in request.FILES:
#             product.product_image1 = request.FILES.get('product_image1', product.product_image1)
#         if 'product_image2' in request.FILES:
#             product.product_image2 = request.FILES.get('product_image2', product.product_image2)
#         if 'product_image3' in request.FILES:
#             product.product_image3 = request.FILES.get('product_image3', product.product_image3)

#         # Save the updated book
#         product.save()

#         return redirect('admin_dashboard')  # Redirect to the same page or another page
#     return render(request, 'admin1/update_item.html')
# def update_item(request):
#     main_category= MainCategory.objects.all()
#     sub_category= SubCategory.objects.all()
#     manufacturer = Manufacturer.objects.all()
#     context={
#         'main_category':main_category,
#         'sub_category':sub_category,
#         'manufacturer':manufacturer,
        
        
#     }

#     if request.method == 'POST':
#         search_name = request.POST.get('search_name')  # Separate search name for clarity
#         product = get_object_or_404(Product, name=search_name)
        
        

#         # Track if any changes were made
#         changes_made = False

#         # Update fields only if provided
#         if 'name' in request.POST:
#             product.name = request.POST['name']
#             changes_made = True
#         if 'main_category' in request.POST:
#             product.main_category = request.POST['main_category']
#             changes_made = True
#         if 'sub_category' in request.POST:
#             product.sub_category = request.POST['sub_category']
#             changes_made = True
#         if 'product_stock' in request.POST:
#             product.product_stock = int(request.POST.get('product_stock', '0') or 0)
#             changes_made = True
#         if 'discount_price' in request.POST:
#             product.discount_price = float(request.POST.get('discount_price', '0') or 0.0)
#             changes_made = True
#         if 'actual_price' in request.POST:
#             product.actual_price = float(request.POST.get('actual_price', '0') or 0.0)
#             changes_made = True
#         if 'image_url' in request.POST:
#             product.image_url = request.POST['image_url']
#             changes_made = True
#         if 'site_link' in request.POST:
#             product.site_link = request.POST['site_link']
#             changes_made = True
#         # if 'ratings' in request.POST:
#         #     product.ratings = request.POST['ratings']
#         #     changes_made = True
#         if 'ratings' in request.POST:
#             product.ratings = int(request.POST.get('ratings', '0') or 0)
#             changes_made = True
#         if 'no_of_ratings' in request.POST:
#             product.no_of_ratings = request.POST['no_of_ratings']
#             changes_made = True

#         # Save only if changes were made
#         if changes_made:
#             product.save()
#             return redirect('admin_dashboard')
#         else:
#             message = "No changes were made to the product."
#             return render(request, 'admin1/update_item.html', {'message': message})
   

    
#     return render(request, 'admin1/update_item.html',context)
      

   
# def list_item(request):
#     product = Product.objects.all()
#     return render(request,'admin1/list_item.html',{'product':product})
def list_item(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 9)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin1/list_item.html', {'page_obj': page_obj})

    #return render(request, 'admin1/list_item.html')
# def slide(request):
#     if request.method == 'POST':
#         add_head = request.POST.get('add_head')
#         add_sub_head = request.POST.get('add_sub_head')
#         add_text = request.POST.get('add_text')
#         add_price = request.POST.get('add_price')
#         add_image = request.FILES.get('add_image')
       

#         slider = Slider(
#             add_head=add_head,
#             add_sub_head=add_sub_head,
#             add_text=add_text,
#             add_price=add_price,
#             add_image=add_image,
            
#         )
#         slider.save()
#         # show in home app inner index page in 4 houre
#         response.set_cookie('add_head', add_head, max_age=14400)
#         response.set_cookie('add_sub_head', add_sub_head, max_age=14400)
#         response.set_cookie('add_text', add_text, max_age=14400)
#         response.set_cookie('add_price', add_price, max_age=14400)
#         response.set_cookie('add_image', add_image, max_age=14400)
#         return redirect('admin1/add_item.html')
        
#     return render(request, 'admin1/slide.html')

def slide(request):
    if request.method == 'POST':
        add_head = request.POST.get('add_head')
        add_sub_head = request.POST.get('add_sub_head')
        add_text = request.POST.get('add_text')
        add_price = request.POST.get('add_price')
        add_image = request.FILES.get('add_image')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        # Save the slider data in the database
        slider = Slider(
            add_head=add_head,
            add_sub_head=add_sub_head,
            add_text=add_text,
            add_price=add_price,
            add_image=add_image,
            start_time=start_time,
            end_time=end_time
        )
        slider.save()

        return redirect('slide')

       

    return render(request, 'admin1/slide.html')

    
   
# def add_category(request):
#     return render(request, 'add_category.html')
# def delete_category(request):
#     return render(request, 'delete_category.html')
# def update_item(request):
#     main_category= MainCategory.objects.all()
#     sub_category= SubCategory.objects.all()
#     manufacturer = Manufacturer.objects.all()
   
#     search = request.GET.get('search_name')
#     product = get_object_or_404(Product, name =search)
#     context={
#         'main_category':main_category,
#         'sub_category':sub_category,
#         'manufacturer':manufacturer,
#         'product':product

#     }
#     if request.method == 'POST':

#         name = request.POST.get('name',product.name)
#         main_category=request.POST.get('main_category')
#         main_category = get_object_or_404(MainCategory, name=main_category)
#         sub_category=request.POST.get('sub_category')
#         sub_category = get_object_or_404(SubCategory, name=sub_category)
#         manufacturer=request.POST.get('manufacturer')
#         manufacturer = get_object_or_404(Manufacturer, name=manufacturer)
#         image_url=request.POST.get('image_url',product.image_url)
#         site_link=request.POST.get('site_link',product.site_link)
#         ratings = float(request.POST.get('ratings', '0',product.ratings) or 0.0)
#         no_of_ratings = int(request.POST.get('no_of_ratings', '0',product.no_of_ratings) or 0)
#         discount_price = float(request.POST.get('discount_price', '0',product.discount_price) or 0.0)
#         actual_price = float(request.POST.get('actual_price', '0',product.actual_price) or 0.0)
#         product_stock = int(request.POST.get('product_stock', '0',product.product_stock) or 0)


#         product.save()




#     return render(request, 'admin1/upadate_item.html',context)
# def update_item(request):
#     main_category = MainCategory.objects.all()
#     sub_category = SubCategory.objects.all()
#     manufacturer = Manufacturer.objects.all()

#     search = request.GET.get('search_name')  # Ensure matches form input name
#     product = None

#     if search:
#         try:
#             product = Product.objects.get(name=search)
#         except Product.DoesNotExist:
#             return render(request, 'admin1/update_item.html', {
#                 'error_message': 'Product not found',
#                 'main_category': main_category,
#                 'sub_category': sub_category,
#                 'manufacturer': manufacturer
#             })

#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         product = get_object_or_404(Product, id=product_id)

#         name = request.POST.get('name', product.name)
#         main_category = get_object_or_404(MainCategory, id=request.POST.get('main_category', product.main_category.id))
#         sub_category = get_object_or_404(SubCategory, id=request.POST.get('sub_category', product.sub_category.id))
#         manufacturer = get_object_or_404(Manufacturer, id=request.POST.get('manufacturer', product.manufacturer.id))
#         image_url = request.POST.get('image_url', product.image_url)
#         site_link = request.POST.get('site_link', product.site_link)
#         ratings = float(request.POST.get('ratings', product.ratings or 0))
#         no_of_ratings = int(request.POST.get('no_of_ratings', product.no_of_ratings or 0))
#         discount_price = float(request.POST.get('discount_price', product.discount_price or 0.0))
#         actual_price = float(request.POST.get('actual_price', product.actual_price or 0.0))
#         product_stock = int(request.POST.get('product_stock', product.product_stock or 0))
#         product.name = name
#         product.manufacturer = manufacturer
#         product.main_category = main_category
#         product.sub_category = sub_category
#         product.image_url = image_url
#         product.site_link = site_link
#         product.ratings = ratings
#         product.no_of_ratings = no_of_ratings
#         product.discount_price = discount_price
#         product.actual_price = actual_price
#         product.product_stock = product_stock

    

#         product.save()

#     return render(request, 'admin1/update_item.html', {
#         'main_category': main_category,
#         'sub_category': sub_category,
#         'manufacturer': manufacturer,
#         'product': product
#     })

# def update_item(request):
#     main_category = MainCategory.objects.all()
#     sub_category = SubCategory.objects.all()
#     manufacturer = Manufacturer.objects.all()
#     
    
    
    
#     if request.method == 'POST':
#         search = request.GET.get('search_name')  # Fixed variable name
#         print('search')
#         product = None
#         print('search1')
#         if search:
#              product = get_object_or_404(Product, name=search)
#              print('product')
#         name = request.POST.get('name', product.name)
#         main_category = get_object_or_404(MainCategory, name=request.POST.get('main_category'))
#         sub_category = get_object_or_404(SubCategory, name=request.POST.get('sub_category'))
#         manufacturer = get_object_or_404(Manufacturer, name=request.POST.get('manufacturer'))
#         image_url = request.POST.get('image_url', product.image_url)
#         site_link = request.POST.get('site_link', product.site_link)
#         ratings = float(request.POST.get('ratings', product.ratings) or 0.0)
#         no_of_ratings = int(request.POST.get('no_of_ratings', product.no_of_ratings) or 0)
#         discount_price = float(request.POST.get('discount_price', product.discount_price) or 0.0)
#         actual_price = float(request.POST.get('actual_price', product.actual_price) or 0.0)
#         product_stock = int(request.POST.get('product_stock', product.product_stock) or 0)

#         # Update the product fields
#         product.name = name
#         product.manufacturer = manufacturer
#         product.main_category = main_category
#         product.sub_category = sub_category
#         product.image_url = image_url
#         product.site_link = site_link
#         product.ratings = ratings
#         product.no_of_ratings = no_of_ratings
#         product.discount_price = discount_price
#         product.actual_price = actual_price
#         product.product_stock = product_stock

#         product.save()  # Fixed: Save the updated product

#     context = {
#         'main_category': main_category,
#         'sub_category': sub_category,
#         'manufacturer': manufacturer,
#         'product': product
#     }

#     return render(request, 'admin1/update_item.html', context)




# def update_item(request):
#     main_category = MainCategory.objects.all()
#     sub_category = SubCategory.objects.all()
#     manufacturer_list = Manufacturer.objects.all()  # Keep a separate variable for the queryset
#     product = None  

#     if request.method == 'POST':
#         search = request.POST.get('search_name')  

#         if search:
#             try:
#                 product = Product.objects.get(name=search)  
#             except Product.DoesNotExist:
#                 return render(request, 'admin1/update_item.html', {'error': 'Product not found', 'manufacturer': manufacturer_list, 'main_category': main_category, 'sub_category': sub_category})

#         if request.method == 'POST' and product:
#             name = request.POST.get('name', product.name)
#             main_category_name = request.POST.get('main_category')
#             sub_category_name = request.POST.get('sub_category')
#             manufacturer_name = request.POST.get('manufacturer')

#             main_category_obj = get_object_or_404(MainCategory, id=main_category_name) if main_category_name else product.main_category
#             sub_category_obj = get_object_or_404(SubCategory, id=sub_category_name) if sub_category_name else product.sub_category
#             manufacturer_obj = get_object_or_404(Manufacturer, id=manufacturer_name) if manufacturer_name else product.manufacturer

#             image_url = request.POST.get('image_url', product.image_url)
#             site_link = request.POST.get('site_link', product.site_link)
#             ratings = float(request.POST.get('ratings', product.ratings) or 0.0)
#             no_of_ratings = int(request.POST.get('no_of_ratings', product.no_of_ratings) or 0)
#             discount_price = float(request.POST.get('discount_price', product.discount_price) or 0.0)
#             actual_price = float(request.POST.get('actual_price', product.actual_price) or 0.0)
#             product_stock = int(request.POST.get('product_stock', product.product_stock) or 0)

#             product.name = name
#             product.manufacturer = manufacturer_obj
#             product.main_category = main_category_obj
#             product.sub_category = sub_category_obj
#             product.image_url = image_url
#             product.site_link = site_link
#             product.ratings = ratings
#             product.no_of_ratings = no_of_ratings
#             product.discount_price = discount_price
#             product.actual_price = actual_price
            
#             product.product_stock = product_stock
#             print('product all get ')
#             print('product id :', product.id)

#             product.save()  
#             print('product updated id :', product.id)
#             print('updated product',product.discount_price)



#     context = {
#         'main_category': main_category,
#         'sub_category': sub_category,
#         'manufacturer': manufacturer_list,  # Use the original queryset
#         'product': product
#     }

#     return render(request, 'admin1/update_item.html', context)


# def update_item(request):
#     # Initialize context with common data
#     context = {
#         'main_category': MainCategory.objects.all(),
#         'sub_category': SubCategory.objects.all(),
#         'manufacturer': Manufacturer.objects.all(),
#         'product': None,
#         'message': None
#     }

#     # Handle autocomplete
#     if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))
#         titles = [product.name for product in qs][:10]
#         return JsonResponse(titles, safe=False)

#     # Handle search
#     if 'search_name' in request.POST:
#         search_name = request.POST.get('search_name')
#         try:
#             product = Product.objects.get(name=search_name)
#             context['product'] = product
#         except Product.DoesNotExist:
#             context['message'] = f"Product '{search_name}' not found."
#             return render(request, 'admin1/update_item.html', context)

#     # Handle update
#     if request.method == 'POST' and 'update_product' in request.POST:
#         try:
#             product = Product.objects.get(id=request.POST.get('product_id'))
            
#             # Update foreign key fields
#             manufacturer = get_object_or_404(Manufacturer, id=request.POST.get('manufacturer'))
#             main_category = get_object_or_404(MainCategory, id=request.POST.get('main_category'))
#             sub_category = get_object_or_404(SubCategory, id=request.POST.get('sub_category'))

#             # Update text fields
#             product.name = request.POST.get('name')
#             product.image_url = request.POST.get('image_url')
#             product.site_link = request.POST.get('site_link')
            
#             # Update numeric fields with error handling
#             try:
#                 product.ratings = float(request.POST.get('ratings', 0))
#                 product.no_of_ratings = int(request.POST.get('no_of_ratings', 0))
#                 product.discount_price = float(request.POST.get('discount_price', 0))
#                 product.actual_price = float(request.POST.get('actual_price', 0))
#                 product.product_stock = int(request.POST.get('product_stock', 0))
#             except ValueError:
#                 context['message'] = "Invalid numeric values provided"
#                 return render(request, 'admin1/update_item.html', context)

#             # Update relationships
#             product.manufacturer = manufacturer
#             product.main_category = main_category
#             product.sub_category = sub_category

#             product.save()
#             context['message'] = "Product updated successfully"
#             context['product'] = product

#         except Product.DoesNotExist:
#             context['message'] = "Product not found"
#         except Exception as e:
#             context['message'] = f"Error updating product: {str(e)}"

#     return render(request, 'admin1/update_item.html', context)

# def update_item(request):
     
     
#      # Handle search functionality
#      search = request.POST.get('search_name')
     

#      # Try to find the book using search_name
#      product = get_object_or_404(Product, name=search)
#      context = {
#         'main_category': MainCategory.objects.all(),
#         'sub_category': SubCategory.objects.all(),
#         'manufacturer':Manufacturer.objects.all(),
#     }

#      if request.method == 'POST':
          
#                name = request.POST.get('name',product.name)
#                main_category=request.POST.get('main_category')
#                main_category = get_object_or_404(MainCategory, name=main_category)
#                sub_category=request.POST.get('sub_category')
#                sub_category = get_object_or_404(SubCategory, name=sub_category)
#                manufacturer=request.POST.get('manufacturer')
#                manufacturer = get_object_or_404(Manufacturer, name=manufacturer)
#                image_url=request.POST.get('image_url',product.image_url)
#                site_link=request.POST.get('site_link',product.site_link)
#                ratings = float(request.POST.get('ratings', '0',product.ratings) or 0.0)
#                no_of_ratings = int(request.POST.get('no_of_ratings', '0',product.no_of_ratings) or 0)
#                discount_price = float(request.POST.get('discount_price', '0',product.discount_price) or 0.0)
#                actual_price = float(request.POST.get('actual_price', '0',product.actual_price) or 0.0)
#                product_stock = int(request.POST.get('product_stock', '0',product.product_stock) or 0)



#                product.save()

        
               
         
     
#      return render(request, 'admin1/update_item.html',context)

# def update_item(request):
#     if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     # Handle search functionality
#      search = request.POST.get('search_name')
#      if search:
#          search_products = Product.objects.filter(name__icontains=search)
#          if not search_products.exists():
#              error_message = f"No products found for '{search}'."
#              return render(request, 'admin1/update_item.html', {'error_message': error_message})
#      else:
#          search_products = None

#     # Get the product to update
#     product = get_object_or_404(Product, name=search)  # Assuming you're using `name` to find the product

#     if request.method == 'POST':
#         # Update only the fields that are provided in the POST request
#         fields_updated = False
#         if 'name' in request.POST and request.POST.get('name'):
#             product.name = request.POST.get('name')
#             fields_updated = True
#         if 'main_category' in request.POST and request.POST.get('main_category'):
#             product.main_category = request.POST.get('main_category')
#             fields_updated = True
#         if 'sub_category' in request.POST and request.POST.get('sub_category'):
#             product.sub_category = request.POST.get('sub_category')
#             fields_updated = True
#         if 'manufacturer' in request.POST and request.POST.get('manufacturer'):
#             product.manufacturer = request.POST.get('manufacturer')
#             fields_updated = True
#         if 'image_url' in request.POST and request.POST.get('image_url'):
#             product.image_url = request.POST.get('image_url')
#             fields_updated = True
#         if 'site_link' in request.POST and request.POST.get('site_link'):
#             product.site_link = request.POST.get('site_link')
#             fields_updated = True
#         if 'ratings' in request.POST and request.POST.get('ratings'):
#             product.ratings = float(request.POST.get('ratings'))
#             fields_updated = True
#         if 'no_of_ratings' in request.POST and request.POST.get('no_of_ratings'):
#             product.no_of_ratings = int(request.POST.get('no_of_ratings'))
#             fields_updated = True
#         if 'product_stock' in request.POST and request.POST.get('product_stock'):
#             product.product_stock = int(request.POST.get('product_stock'))
#             fields_updated = True
#         if 'discount_price' in request.POST and request.POST.get('discount_price'):
#             product.discount_price = float(request.POST.get('discount_price'))
#             fields_updated = True
#         if 'actual_price' in request.POST and request.POST.get('actual_price'):
#              new_actual_price = float(request.POST.get('actual_price'))
#              if product.actual_price != new_actual_price:
#                 product.actual_price = new_actual_price
#                 fields_updated = True
#                 print(f"Updated actual_price to: {new_actual_price}")
#              else:
#                 print("Actual price is the same; no update needed.")

#         if fields_updated:
#             product.save()  # Save only if at least one field was updated
#             success_message = "Product updated successfully."
#         else:
#             success_message = "No fields were updated."

#         context = {
#             'success_message': success_message,
#             'search_products': search_products,
#         }
#         return render(request, 'admin1/update_item.html', context)

#     # Render the update page
#     context = {
#         'search_products': search_products,
#     }
#     return render(request, 'admin1/update_item.html', context)
# def update_item(request):
#     # Autocomplete functionality
#     if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))
#         titles = [product.name for product in qs][:10]
#         return JsonResponse(titles, safe=False)

#     search_products = None
#     product = None  # Initialize product to None

#     if request.method == 'POST':  # Handle form submission
#         search = request.POST.get('search_name')
#         if search:
#             search_products = Product.objects.filter(name__icontains=search)
#             if not search_products.exists():
#                 error_message = f"No products found for '{search}'."
#                 return render(request, 'admin1/update_item.html', {'error_message': error_message})
#             # If only one product matches, pre-select it
#             if search_products.count() == 1:
#                 product = search_products.first()

#     if 'product_id' in request.GET:  # If a product_id is provided
#         product = get_object_or_404(Product, id=request.GET['product_id'])

#     if request.method == 'POST' and product:
#         fields_updated = False
#         success_message = ""

#         # Define updatable fields and their types
#         updatable_fields = {
#             'name': str,
#             'main_category': str,
#             'sub_category': str,
#             'manufacturer': str,
#             'image_url': str,
#             'site_link': str,
#             'ratings': float,
#             'no_of_ratings': int,
#             'product_stock': int,
#             'discount_price': float,
#             'actual_price': float,
#         }

#         # Update product fields dynamically
#         for field, field_type in updatable_fields.items():
#             if field in request.POST and request.POST.get(field):
#                 new_value = field_type(request.POST.get(field))
#                 if getattr(product, field) != new_value:
#                     setattr(product, field, new_value)
#                     fields_updated = True

#         if fields_updated:
#             product.save()  # Save only if at least one field was updated
#             success_message = f"Product '{product.name}' updated successfully."
#         else:
#             success_message = "No fields were updated."

#         return render(request, 'admin1/update_item.html', {
#             'success_message': success_message,
#             'search_products': search_products,
#             'product': product,
#         })

#     return render(request, 'admin1/update_item.html', {'search_products': search_products, 'product': product})

    # # If no product is found, return with an error
    # if not product:
    #     return render(request, 'admin1/update_item.html', {'error_message': 'Product not found.'})

    # Render the update page
    # context = {
    #     'search_products': search_products,
    #     'product': product,  # Pass the product object for editing
    # }
    # return render(request, 'admin1/update_item.html', context)



# def update_item(request):
#     # ✅ Autocomplete functionality
#     if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     product = None
#     search_products = None
#     error_message = None
#     success_message = None

#     # ✅ Search functionality
#     search = request.POST.get('search_name')
#     if search:
#         search_products = Product.objects.filter(name__icontains=search)
#         if not search_products.exists():
#             error_message = f"No products found for '{search}'."
#             return render(request, 'admin1/update_item.html', {'error_message': error_message})

#     # ✅ Fetch product using `product_id` if available
#     product_id = request.GET.get('product_id')
#     if product_id:
#         product = get_object_or_404(Product, id=product_id)
#     elif search_products and search_products.count() == 1:
#         product = search_products.first()

#     if not product:
#         error_message = "No product found for the given search criteria."
#         return render(request, 'admin1/update_item.html', {'error_message': error_message})

#     # ✅ Handle product update
#     if request.method == 'POST':
#         fields_updated = False
#         update_fields = [
#             'name', 'main_category', 'sub_category', 'manufacturer', 'image_url',
#             'site_link', 'ratings', 'no_of_ratings', 'product_stock',
#             'discount_price', 'actual_price'
#         ]

#         for field in update_fields:
#             if field in request.POST and request.POST.get(field):
#                 value = request.POST.get(field)
#                 # Convert values where necessary
#                 if field in ['ratings', 'discount_price', 'actual_price']:
#                     value = float(value)
#                 elif field in ['no_of_ratings', 'product_stock']:
#                     value = int(value)
                
#                 setattr(product, field, value)
#                 fields_updated = True

#         if fields_updated:
#             product.save()
#             success_message = "Product updated successfully."
#         else:
#             success_message = "No fields were updated."

#     # ✅ Return updated context
#     context = {
#         'success_message': success_message,
#         'error_message': error_message,
#         'search_products': search_products,
#         'product': product,
#     }
#     return render(request, 'admin1/update_item.html', context)


# def update_item(request):
#     # ✅ Autocomplete functionality
#     if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     product = None
#     search_products = None
#     error_message = None

#     # ✅ If product ID is passed in GET request (after clicking search result)
#     product_id = request.GET.get('product_id')
#     if product_id:
#         product = get_object_or_404(Product, id=product_id)

#     # ✅ Search functionality
#     search = request.POST.get('search_name')
#     if search:
#         search_products = Product.objects.filter(name__icontains=search)
#         if not search_products.exists():
#             error_message = f"No products found for '{search}'."
#         return render(request, 'admin1/update_item.html', {
#             'error_message': error_message,
#             'search_products': search_products
#         })
#     product = get_object_or_404(Product, name=search)
#     # ✅ Updating the product
#     if request.method == 'POST' and product:
#         product.name = request.POST.get('name', product.name)
#         product.manufacturer = request.POST.get('manufacturer', product.manufacturer)
#         product.main_category = request.POST.get('main_category', product.main_category)
#         product.sub_category = request.POST.get('sub_category', product.sub_category)
#         product.image_url = request.POST.get('image_url', product.image_url)
#         product.site_link = request.POST.get('site_link', product.site_link)
#         product.ratings = request.POST.get('ratings', product.ratings)
#         product.no_of_ratings = request.POST.get('no_of_ratings', product.no_of_ratings)
#         product.discount_price = request.POST.get('discount_price', product.discount_price)
#         product.actual_price = request.POST.get('actual_price', product.actual_price)
#         product.product_stock = request.POST.get('product_stock', product.product_stock)

#         product.save()
#         return redirect('admin_dashboard')  # Redirect after updating

#     return render(request, 'admin1/update_item.html', {
#         'product': product,
#         'search_products': search_products
#     })


# def update_item(request):
#     # ✅ Autocomplete functionality
#     if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))
#         titles = [product.name for product in qs]
#         return JsonResponse(titles, safe=False)

#     product = None
#     search_products = None
#     error_message = None

#     # ✅ If product ID is passed in GET request (after clicking search result)
#     product_id = request.GET.get('product_id')
#     if product_id:
#         product = get_object_or_404(Product, id=product_id)

#     # ✅ Search functionality
#     if request.method == 'POST':
#         search = request.POST.get('search_name')
#         if search:
#             search_products = Product.objects.filter(name__icontains=search)
#             if not search_products.exists():
#                 error_message = f"No products found for '{search}'."
#             else:
#                 return render(request, 'admin1/update_item.html', {
#                     'error_message': error_message,
#                     'search_products': search_products
#                 })

#     # ✅ If a product is selected for updating
#     if request.method == 'POST' and product:
#         product.name = request.POST.get('name', product.name)
#         product.manufacturer = request.POST.get('manufacturer', product.manufacturer)
#         product.main_category = request.POST.get('main_category', product.main_category)
#         product.sub_category = request.POST.get('sub_category', product.sub_category)
#         product.image_url = request.POST.get('image_url', product.image_url)
#         product.site_link = request.POST.get('site_link', product.site_link)
#         product.ratings = request.POST.get('ratings', product.ratings)
#         product.no_of_ratings = request.POST.get('no_of_ratings', product.no_of_ratings)
#         product.discount_price = request.POST.get('discount_price', product.discount_price)
#         product.actual_price = request.POST.get('actual_price', product.actual_price)
#         product.product_stock = request.POST.get('product_stock', product.product_stock)

#         # Save the updated product
#         product.save()
#         return redirect('admin_dashboard')  # Redirect after updating

#     return render(request, 'admin1/update_item.html', {
#         'product': product,
#         'search_products': search_products,
#         'error_message': error_message
#     })




# def edit_slide(request):
#     if 'term' in request.GET:
#         qs = Slider.objects.filter(add_head__icontains=request.GET.get('term'))
#         titles = [slider.add_head for slider in qs][:10]
#         return JsonResponse(titles, safe=False)

#     context = {
#         'slider': None,
#         'message': None
#     }

#     if request.method == 'POST':
#         if 'search_name' in request.POST:
#             search_name = request.POST.get('search_name')
#             try:
#                 slider = Slider.objects.get(add_head=search_name)
#                 context['slider'] = slider
#             except Slider.DoesNotExist:
#                 context['message'] = f"Slide '{search_name}' not found."
#                 return render(request, 'admin1/edit_slide.html', context)

#         elif 'update_slide' in request.POST:
#             try:
#                 slider = Slider.objects.get(id=request.POST.get('slider_id'))
#                 slider.add_head = request.POST.get('add_head')
#                 slider.add_sub_head = request.POST.get('add_sub_head')
#                 slider.add_text = request.POST.get('add_text')
#                 slider.add_price = float(request.POST.get('add_price', 0))
#                 slider.start_time = request.POST.get('start_time')
#                 slider.end_time = request.POST.get('end_time')
                
#                 if 'add_image' in request.FILES:
#                     slider.add_image = request.FILES['add_image']
                
#                 slider.save()
#                 context['message'] = "Slide updated successfully"
#                 context['slider'] = slider
#             except Exception as e:
#                 context['message'] = f"Error updating slide: {str(e)}"

#     return render(request, 'admin1/edit_slide.html', context)

# def delete_slide(request):
#     if 'term' in request.GET:
#         qs = Slider.objects.filter(add_head__icontains=request.GET.get('term'))
#         titles = [slider.add_head for slider in qs][:10]
#         return JsonResponse(titles, safe=False)

#     context = {
#         'slider': None,
#         'message': None,
#         'confirm': False
#     }

#     if request.method == 'POST':
#         if 'search_name' in request.POST:
#             search_name = request.POST.get('search_name')
#             try:
#                 slider = Slider.objects.get(add_head=search_name)
#                 context['slider'] = slider
#                 context['confirm'] = True
#             except Slider.DoesNotExist:
#                 context['message'] = f"Slide '{search_name}' not found."

#         elif 'confirm_delete' in request.POST:
#             slider_id = request.POST.get('slider_id')
#             try:
#                 slider = Slider.objects.get(id=slider_id)
#                 slider.delete()
#                 context['message'] = f"Slide '{slider.add_head}' deleted successfully."
#             except Slider.DoesNotExist:
#                 context['message'] = "Slide not found."
#             except Exception as e:
#                 context['message'] = f"Error deleting slide: {str(e)}"

#     return render(request, 'admin1/delete_slide.html', context)

def edit_slide(request):
    # Get all slides for display
    all_slides = Slider.objects.all().order_by('-start_time')
    
    context = {
        'slider': None,
        'message': None,
        'all_slides': all_slides
    }

    if request.method == 'POST':
        if 'slider_id' in request.POST:
            try:
                slider = Slider.objects.get(id=request.POST.get('slider_id'))
                if 'update_slide' in request.POST:
                    # Update the slider
                    slider.add_head = request.POST.get('add_head')
                    slider.add_sub_head = request.POST.get('add_sub_head')
                    slider.add_text = request.POST.get('add_text')
                    slider.add_price = float(request.POST.get('add_price', 0))
                    slider.start_time = request.POST.get('start_time')
                    slider.end_time = request.POST.get('end_time')
                    
                    if 'add_image' in request.FILES:
                        slider.add_image = request.FILES['add_image']
                    
                    slider.save()
                    context['message'] = "Slide updated successfully"
                else:
                    # Just load the slider for editing
                    context['slider'] = slider
            except Exception as e:
                context['message'] = f"Error: {str(e)}"

    return render(request, 'admin1/edit_slide.html', context)

def delete_slide(request):
    # Get all slides for display
    all_slides = Slider.objects.all().order_by('-start_time')
    
    context = {
        'slider': None,
        'message': None,
        'confirm': False,
        'all_slides': all_slides
    }

    if request.method == 'POST':
        if 'slider_id' in request.POST:
            try:
                slider = Slider.objects.get(id=request.POST.get('slider_id'))
                if 'confirm_delete' in request.POST:
                    # Delete the slider
                    slider_head = slider.add_head
                    slider.delete()
                    context['message'] = f"Slide '{slider_head}' deleted successfully."
                else:
                    # Show confirmation
                    context['slider'] = slider
                    context['confirm'] = True
            except Exception as e:
                context['message'] = f"Error: {str(e)}"

    return render(request, 'admin1/delete_slide.html', context)



# def delete_item(request):
#     # Handle autocomplete
#     if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))
#         titles = [product.name for product in qs][:10]
#         return JsonResponse(titles, safe=False)

#     # Get all items for display
#     all_items = Product.objects.all().order_by('-id')
    
#     context = {
#         'product': None,
#         'message': None,
#         'confirm': False,
#         'all_items': all_items
#     }

#     if request.method == 'POST':
#         if 'search_name' in request.POST:
#             search_name = request.POST.get('search_name')
#             try:
#                 all_items = Product.objects.filter(name__icontains=search_name)
#                 context['all_items'] = all_items
#             except Exception as e:
#                 messages.error(request, f"Error: {str(e)}")
        
#         elif 'item_id' in request.POST:
#             try:
#                 product = Product.objects.get(id=request.POST.get('item_id'))
#                 if 'confirm_delete' in request.POST:
#                     # Delete the product
#                     product_name = product.name
#                     product.delete()
#                     messages.success(request, f"Product '{product_name}' deleted successfully.")
#                 else:
#                     # Show confirmation
#                     context['product'] = product
#                     context['confirm'] = True
#             except Exception as e:
#                 messages.error(request, f"Error: {str(e)}")

#     return render(request, 'admin1/delete_item.html', context)

# def update_item(request):
#     # Handle autocomplete
#     if 'term' in request.GET:
#         qs = Product.objects.filter(name__icontains=request.GET.get('term'))
#         titles = [product.name for product in qs][:10]
#         return JsonResponse(titles, safe=False)

#     # Get all items for display
#     all_items = Product.objects.all().order_by('-id')
    
#     context = {
#         'product': None,
#         'message': None,
#         'all_items': all_items,
#         'main_category': MainCategory.objects.all(),
#         'sub_category': SubCategory.objects.all(),
#         'manufacturer': Manufacturer.objects.all()
#     }

#     if request.method == 'POST':
#         if 'search_name' in request.POST:
#             search_name = request.POST.get('search_name')
#             try:
#                 all_items = Product.objects.filter(name__icontains=search_name)
#                 context['all_items'] = all_items
#             except Exception as e:
#                 context['message'] = f"Error: {str(e)}"
        
#         elif 'item_id' in request.POST:
#             try:
#                 product = Product.objects.get(id=request.POST.get('item_id'))
#                 if 'update_item' in request.POST:
#                     # Update the product
#                     product.name = request.POST.get('name')
#                     product.main_category = MainCategory.objects.get(id=request.POST.get('main_category'))
#                     product.sub_category = SubCategory.objects.get(id=request.POST.get('sub_category'))
#                     product.manufacturer = Manufacturer.objects.get(id=request.POST.get('manufacturer'))
#                     product.product_stock = int(request.POST.get('product_stock'))
#                     product.actual_price = float(request.POST.get('actual_price'))
#                     product.discount_price = float(request.POST.get('discount_price'))
#                     product.image_url = request.POST.get('image_url')
#                     product.site_link = request.POST.get('site_link')
                    
#                     product.save()
#                     context['message'] = "Product updated successfully"
#                 else:
#                     # Just load the product for editing
#                     context['product'] = product
#             except Exception as e:
#                 context['message'] = f"Error: {str(e)}"

#     return render(request, 'admin1/update_item.html', context)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def delete_item(request):
    # Handle autocomplete
    if 'term' in request.GET:
        qs = Product.objects.filter(name__icontains=request.GET.get('term'))
        titles = [product.name for product in qs][:10]
        return JsonResponse(titles, safe=False)

    # Get items list
    items_list = Product.objects.all().order_by('-id')
    
    # Handle search
    if request.method == 'POST' and 'search_name' in request.POST:
        search_name = request.POST.get('search_name')
        if search_name:
            items_list = items_list.filter(name__icontains=search_name)

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(items_list, 10)  # Show 10 items per page
    
    try:
        all_items = paginator.page(page)
    except PageNotAnInteger:
        all_items = paginator.page(1)
    except EmptyPage:
        all_items = paginator.page(paginator.num_pages)
    
    context = {
        'product': None,
        'message': None,
        'confirm': False,
        'all_items': all_items,
        'is_paginated': True if paginator.num_pages > 1 else False
    }

    if request.method == 'POST' and 'item_id' in request.POST:
        try:
            product = Product.objects.get(id=request.POST.get('item_id'))
            if 'confirm_delete' in request.POST:
                product_name = product.name
                product.delete()
                messages.success(request, f"Product '{product_name}' deleted successfully.")
            else:
                context['product'] = product
                context['confirm'] = True
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

    return render(request, 'admin1/delete_item.html', context)

def update_item(request):
    # Handle autocomplete
    if 'term' in request.GET:
        qs = Product.objects.filter(name__icontains=request.GET.get('term'))
        titles = [product.name for product in qs][:10]
        return JsonResponse(titles, safe=False)

    # Get items list
    items_list = Product.objects.all().order_by('-id')
    
    # Handle search
    if request.method == 'POST' and 'search_name' in request.POST:
        search_name = request.POST.get('search_name')
        if search_name:
            items_list = items_list.filter(name__icontains=search_name)

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(items_list, 10)  # Show 10 items per page
    
    try:
        all_items = paginator.page(page)
    except PageNotAnInteger:
        all_items = paginator.page(1)
    except EmptyPage:
        all_items = paginator.page(paginator.num_pages)
    
    context = {
        'product': None,
        'message': None,
        'all_items': all_items,
        'main_category': MainCategory.objects.all(),
        'sub_category': SubCategory.objects.all(),
        'manufacturer': Manufacturer.objects.all(),
        'is_paginated': True if paginator.num_pages > 1 else False
    }

    if request.method == 'POST' and 'item_id' in request.POST:
        try:
            product = Product.objects.get(id=request.POST.get('item_id'))
            if 'update_item' in request.POST:
                # Update the product
                product.name = request.POST.get('name')
                product.main_category = MainCategory.objects.get(id=request.POST.get('main_category'))
                product.sub_category = SubCategory.objects.get(id=request.POST.get('sub_category'))
                product.manufacturer = Manufacturer.objects.get(id=request.POST.get('manufacturer'))
                product.product_stock = int(request.POST.get('product_stock'))
                product.actual_price = float(request.POST.get('actual_price'))
                product.discount_price = float(request.POST.get('discount_price'))
                product.image_url = request.POST.get('image_url')
                product.site_link = request.POST.get('site_link')
                
                product.save()
                context['message'] = "Product updated successfully"
            else:
                context['product'] = product
        except Exception as e:
            context['message'] = f"Error: {str(e)}"

    return render(request, 'admin1/update_item.html', context)
