from django.shortcuts import get_object_or_404, render,redirect
from .models import Register,State,District,Account
from django.contrib import messages
from django.urls import reverse
from apps.admin1.models import Product
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
import requests
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from apps.payments.models import Address
from django.contrib.auth import logout as auth_logout 
# Create your views here.
# def login(request):
#      if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             # Try to retrieve the user by email
#             user = Register.objects.get(username=username)

#             # Check the password (adjust this if your passwords are hashed)
#             if user.password == password or check_password(password, user.password):
#                 messages.success(request, 'Login successful')

#                 # login=Login.create()

               

#         except Register.DoesNotExist:
#             messages.warning(request, 'Email does not exist')
#             return redirect('login')
#         return render(request, 'users/login.html')
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             # Retrieve the user by username (ensure username is unique or handle appropriately)
#             user = Register.objects.get(username=username) or Register.objects.get(username='admin1')

#             # Check the password (assuming passwords are hashed using Django's password hashing)
#             if check_password(password, user.password):
#                 # If the password matches, set a success message and proceed
#                 messages.success(request, 'Login successful')
#                 return redirect('index')  # Redirect to a homepage or dashboard after successful login
#             else:
#                 # If the password does not match, show an error message
#                 messages.warning(request, 'Incorrect password')
#                 return redirect('login')  # Redirect back to login page

#         except Register.DoesNotExist:
#             # If the user does not exist, show a warning message
#             messages.warning(request, 'Username does not exist')
#             return redirect('login')  # Redirect back to login page

#     return render(request, 'users/login.html')
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             # Retrieve the user by username (ensure username is unique or handle appropriately)
#             user = Register.objects.get(username=username)

#             if user == 'admin1':


#              # Check the password (assuming passwords are hashed using Django's password hashing)
#              if check_password(password, user.password):
#                 # If the password matches, set a success message and proceed
#                 messages.success(request, 'Login successful')
#                 return redirect('admin_dashboard')  # Redirect to a admin dashboard after successful login
#             elif user != 'admin1':
#                  # Check the password (assuming passwords are hashed using Django's password hashing)
#              if check_password(password, user.password):
#                 # If the password matches, set a success message and proceed
#                 messages.success(request, 'Login successful')
#                 return redirect('login')  # Redirect to a homepage or dashboard after successful login

#             else:
#                 # If the password does not match, show an error message
#                 messages.warning(request, 'Incorrect password')
#                 return redirect('login')  # Redirect back to login page

#         except Register.DoesNotExist:
#             # If the user does not exist, show a warning message
#             messages.warning(request, 'Username does not exist')
#             return redirect('login')  # Redirect back to login page

#     return render(request, 'users/login.html')
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             # Retrieve the user by username
#             user = Register.objects.get(username=username)
            

#             # Check if the password is correct
#             if check_password or password(password, user.password):
#                 # Check if the user is 'admin1' for admin login
                
#                 if username == 'admin1':
#                     messages.success(request, 'Admin login successful')
#                     return redirect('admin_dashboard')  # Redirect to admin dashboard
#                 else:
#                     messages.success(request, 'Login successful')
#                     return redirect('index')  # Redirect to a regular user's homepage
#                try:
#                 user = Register.objects.get(email=email, password=password)
#             # Save user_id in session
#             request.session['user_id'] = user.id
#             request.session['username'] = user.username  # Optional for display purposes
#             messages.success(request, f"Welcome, {user.username}!")
#             return redirect('product_list')  # Redirect to the main page
#         except Register.DoesNotExist:
#             messages.error(request, "Invalid email or password.")
#             return redirect('login')
                
            
#             else:
#                 # Incorrect password
#                 messages.warning(request, 'Incorrect password')
#                 return redirect('login')

#         except Register.DoesNotExist:
#             # User does not exist
#             messages.warning(request, 'Username does not exist')
#             return redirect('login')

#     return render(request, 'users/login.html')
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             # Retrieve the user by username
#             user = Register.objects.get(username=username)

#             # Check if the password matches
#             if check_password or password(password, user.password):
#                 # Check if the user is 'admin1' for admin login
#                 # Check if the user is admin
#                 if username == 'admin1':
#                     messages.success(request, 'Admin login successful')
#                     return redirect('admin_dashboard')  # Redirect to the admin dashboard
                
#                 # Regular user login
#                 request.session['user_id'] = user.id  # Save user ID in the session
#                 request.session['username'] = user.username  # Save username for convenience
#                 messages.success(request, f"Welcome, {user.username}!")
#                 return redirect('index')  # Redirect to the user's homepage
#             else:
#                 # Incorrect password
#                 messages.error(request, 'Incorrect password. Please try again.')
#                 return redirect('login')

#         except Register.DoesNotExist:
#             # User does not exist
#             messages.error(request, 'Username does not exist. Please register first.')
#             return redirect('login')

#     return render(request, 'users/login.html')

   
# def register(request):
#      if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         person = Register(
#             username=username,
#             email=email,
#             password=make_password(password),
           
#         )
#         person.save()
#         return redirect('index')
#      return render(request, 'users/register.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate input fields
        if not username or not email or not password:
            messages.warning(request, 'All fields are required.')
            return redirect('register')

        if len(password) < 6:
            messages.warning(request, 'Password must be at least 6 characters long.')
            return redirect('register')

        # Check if email or username already exists
        if Register.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists. Please choose another one.')
            return redirect('register')

        if Register.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already registered.')
            return redirect('register')
        

        # Create and save the new user
        person = Register(
            username=username,
            email=email,
            password=make_password(password),
        )
        person.save()

        messages.success(request, 'Registration successful! Please log in.')
        return redirect('index')  # Redirect to login or index page after registration

    return render(request, 'registration/register.html')

   
# def account(request):
#     states=State.objects.all()
#     districts=District.objects.all()
#     if request.method == 'POST':
#         firstName = request.POST.get('firstName')
#         lastName = request.POST.get('lastName')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         address2 = request.POST.get('address2')
#         state = request.POST.get('state')
#         district = request.POST.get('district')
#         pin = request.POST.get('pin')
#         # checkbox its optional someone can choose to give or not and choose one and two  options
#         same_address = request.POST.get('same_address') #Shipping address is the same as my billing address
#         save_info = request.POST.get('save_info') #Save this information for next time
#         # if save_info is checked then save the information in session
#         if save_info:
#             request.session['firstName'] = firstName
#             request.session['lastName'] = lastName
#             request.session['username'] = username
#             request.session['email'] = email
#             request.session['phone'] = phone
#             request.session['address'] = address
#             request.session['address2'] = address2
#             request.session['state'] = state
#             request.session['district'] = district
#             request.session['pin'] = pin
#             request.session['same_address'] = same_address
#             request.session['save_info'] = save_info
#             # if same_address is checked then save the information in session
#             if same_address:
#                 request.session['shipping_address'] = address
#                 else:
#     request.session['shipping_address'] = address2
#     return render(request, 'users/account.html', {'states': states, 'districts': districts
#                                                   return render(request, 'users/account.html', {'states': states, 'districts': districts
                                                                                                
       


#     return render(request, 'users/account.html')
# def account(request):
#     # Fetch all states and districts to display in the form
#     states = State.objects.all()
#     districts = District.objects.all()

#     if request.method == 'POST':
#         firstName = request.POST.get('firstName')
#         lastName = request.POST.get('lastName')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         address2 = request.POST.get('address2')
#         state = request.POST.get('state')
#         district = request.POST.get('district')
#         pin = request.POST.get('pin')

#         # Optional checkboxes
#         same_address = request.POST.get('same_address')  # Shipping address same as billing
#         save_info = request.POST.get('save_info')        # Save information for next time

#         shipping_address= Account(firstName=firstName,lastName=lastName,username=username,email=email,phone=phone,address=address,address2=address2,state=state,district=district,pin=pin)

#         # If "Save Info" is checked, save the details in the session
#         if save_info:
#             request.session['firstName'] = firstName
#             request.session['lastName'] = lastName
#             request.session['username'] = username
#             request.session['email'] = email
#             request.session['phone'] = phone
#             request.session['address'] = address
#             request.session['address2'] = address2
#             request.session['state'] = state
#             request.session['district'] = district
#             request.session['pin'] = pin
#             request.session['same_address'] = same_address
#             request.session['save_info'] = save_info

#             shipping_address.save()
            

#         # Handle the "Shipping address is the same as billing address" logic
#         if same_address:
#             request.session['shipping_address'] = address
#         else:
#             request.session['shipping_address'] = address2

#         # Return success or redirect to another page
#         return redirect('index')  # Replace with the actual success page

#     # Render the account page with state and district data
#     return render(request, 'users/account.html', {'states': states, 'districts': districts})



# def account(request):
#     states = State.objects.all()
#     districts = District.objects.all()

#     if request.method == 'POST':
#         firstName = request.POST.get('firstName')
#         lastName = request.POST.get('lastName')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         address2 = request.POST.get('address2')
#         state_id = request.POST.get('state')
#         district_id = request.POST.get('district')
#         pin = request.POST.get('pin')
#         same_address = request.POST.get('same_address')
#         save_info = request.POST.get('save_info')

#         # Validate required fields
#         if not all([firstName, lastName, username, email, phone, address, state_id, district_id, pin]):
#             messages.error(request, "All fields are required.")
#             return render(request, 'users/account.html', {'states': states, 'districts': districts})

#         # Fetch state and district objects
#         state = State.objects.get(id=state_id)
#         district = District.objects.get(id=district_id)

#         # Save account data
#         account = Account(
#             firstName=firstName,
#             lastName=lastName,
#             username=username,
#             email=email,
#             phone=phone,
#             address=address,
#             address2=address2,
#             state=state,
#             district=district,
#             pin=pin,
#         )
#         account.save()

#         # Save info to session if requested
#         if save_info:
#             request.session['account_data'] = {
#                 'firstName': firstName,
#                 'lastName': lastName,
#                 'username': username,
#                 'email': email,
#                 'phone': phone,
#                 'address': address,
#                 'address2': address2,
#                 'state': state.s_name,
#                 'district': district.d_name,
#                 'pin': pin,
#                 'same_address': same_address,
#             }

#         # Determine shipping address
#         shipping_address = address if same_address else address2
#         request.session['shipping_address'] = shipping_address

#         messages.success(request, "Account details saved successfully!")
#         return redirect('index')

#     return render(request, 'users/account.html', {'states': states, 'districts': districts})
# def account(request):
#     states = State.objects.all()
#     district = District.objects.all()
#     context={
#         'states':states,
#         'district':district
#     }

#     if request.method == 'POST':
#         # Retrieve POST data
#         firstName = request.POST.get('firstName')
#         lastName = request.POST.get('lastName')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         address2 = request.POST.get('address2')
#         state_id = request.POST.get('state')
#         district_id = request.POST.get('district')
#         pin = request.POST.get('pin')
#         same_address = request.POST.get('same_address') == 'on'  # Checkbox returns 'on' if checked
#         save_info = request.POST.get('save_info') == 'on'  # Checkbox returns 'on' if checked

#         # Validate required fields
#         if not all([firstName, lastName, username, phone, address, state_id, district_id, pin]):
#             messages.error(request, "All required fields must be filled out.")
#             return render(request, 'users/account.html')
#         # username and email check alredy registerd
#         try:
#            registered_user = Register.objects.get(username=username, email=email)
#         except Register.DoesNotExist:
#             messages.error(request, "Username or Email not registerd.")
#             return render(request, 'users/account.html',context)

#         # Fetch state and district objects safely
#         try:
#             state = State.objects.get(id=state_id)
#         except State.DoesNotExist:
#             messages.error(request, "Invalid state selected.")
#             return render(request, 'users/account.html', context)

#         try:
#             district = District.objects.get(id=district_id, state=state)
#         except District.DoesNotExist:
#             messages.error(request, "Invalid district selected.")
#             return render(request, 'users/account.html', context)

#         # Save account data
#         account = Account(
#             firstName=firstName,
#             lastName=lastName,
#             username=username,
#             email=email,
#             phone=phone,
#             address=address,
#             address2=address2 if address2 else None,
#             state=state,
#             district=district,
#             pin=pin,
#         )
#         account.save()

#         # Save information to the session if requested
#         if save_info:
#             request.session['account_data'] = {
#                 'firstName': firstName,
#                 'lastName': lastName,
#                 'username': username,
#                 'email': email,
#                 'phone': phone,
#                 'address': address,
#                 'address2': address2,
#                 'state_id': state.id,
#                 'district_id': district.id,
#                 'pin': pin,
#                 'same_address': same_address,
#             }

#         # Set shipping address based on "same_address" checkbox
#         shipping_address = address if same_address else (address2 if address2 else None)
#         request.session['shipping_address'] = shipping_address

#         messages.success(request, "Account details saved successfully!")
#         return redirect('index')  # Redirect to the appropriate page

#     return render(request, 'users/account.html', context)

# def account(request):
#     # Fetch states and districts if not already present
#     def fetch_and_store_states_and_districts():
#         api_url = "https://example.com/api/indian-states-districts"  # Replace with actual API URL
#         try:
#             response = requests.get(api_url)
#             response.raise_for_status()  # Raise error if the request fails
#             data = response.json()

#             # Insert data into database
#             for item in data:
#                 state_name = item["state"]
#                 districts = item["districts"]
                
#                 # Create or retrieve the state
#                 state, created = State.objects.get_or_create(name=state_name)
                
#                 # Create or retrieve districts for the state
#                 for district_name in districts:
#                     District.objects.get_or_create(name=district_name, state=state)
#         except requests.exceptions.RequestException as e:
#             messages.error(request, f"Failed to fetch states and districts: {e}")

#     # Check if states are already in the database; if not, fetch them
#     if not State.objects.exists():
#         fetch_and_store_states_and_districts()

#     # Retrieve all states and districts for the form
#     states = State.objects.all()
#     districts = District.objects.all()
#     context = {
#         'states': states,
#         'districts': districts
#     }

#     if request.method == 'POST':
#         # Retrieve POST data
#         firstName = request.POST.get('firstName')
#         lastName = request.POST.get('lastName')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         address2 = request.POST.get('address2')
#         state_id = request.POST.get('state')
#         district_id = request.POST.get('district')
#         pin = request.POST.get('pin')
#         same_address = request.POST.get('same_address') == 'on'  # Checkbox returns 'on' if checked
#         save_info = request.POST.get('save_info') == 'on'  # Checkbox returns 'on' if checked

#         # Validate required fields
#         if not all([firstName, lastName, username, phone, address, state_id, district_id, pin]):
#             messages.error(request, "All required fields must be filled out.")
#             return render(request, 'users/account.html', context)

#         # Check if the username and email are already registered
#         try:
#             registered_user = Register.objects.get(username=username, email=email)
#         except Register.DoesNotExist:
#             messages.error(request, "Username or Email not registered.")
#             return render(request, 'users/account.html', context)

#         # Fetch state and district objects safely
#         try:
#             state = State.objects.get(id=state_id)
#         except State.DoesNotExist:
#             messages.error(request, "Invalid state selected.")
#             return render(request, 'users/account.html', context)

#         try:
#             district = District.objects.get(id=district_id, state=state)
#         except District.DoesNotExist:
#             messages.error(request, "Invalid district selected.")
#             return render(request, 'users/account.html', context)

#         # Save account data
#         account = Account(
#             firstName=firstName,
#             lastName=lastName,
#             username=username,
#             email=email,
#             phone=phone,
#             address=address,
#             address2=address2 if address2 else None,
#             state=state,
#             district=district,
#             pin=pin,
#         )
#         account.save()

#         # Save information to the session if requested
#         if save_info:
#             request.session['account_data'] = {
#                 'firstName': firstName,
#                 'lastName': lastName,
#                 'username': username,
#                 'email': email,
#                 'phone': phone,
#                 'address': address,
#                 'address2': address2,
#                 'state_id': state.id,
#                 'district_id': district.id,
#                 'pin': pin,
#                 'same_address': same_address,
#             }

#         # Set shipping address based on "same_address" checkbox
#         shipping_address = address if same_address else (address2 if address2 else None)
#         request.session['shipping_address'] = shipping_address

#         messages.success(request, "Account details saved successfully!")
#         return redirect('index')  # Redirect to the appropriate page

#     return render(request, 'users/account.html', context)
# @login_required
# def account(request):
#     if request.user.address_set.exists():
#       users =  get_object_or_404()
    

#       return render(request, 'registration/account.html')




# def logout(request):
#     # Clear the session data
#     request.session.clear()
#     return render(request, 'users/logout.html')
# def logout(request):
#     # Clear the session data
#     request.session.clear()
#     # Add a success message to inform the user
#     messages.success(request, 'You have been logged out successfully.')
#     # Redirect to the login page or home page
#     return redirect('login')  # Replace 'login' with the name of your login page's URL pattern
# def logout(request):
#     # request.session.flush()  # Clear all session data
    
#     messages.success(request, 'You have been logged out.')
#     return redirect('login')  # Redirect to the login page
# def logout(request):
#     # Check if the user is logged in via your custom user model
#     if 'user_id' in request.session:
#         # Remove only your custom session data
#         logout_user = request.session.pop('user_id')
#         del request.session['user_id']
#         del request.session['username']
#         messages.success(request, "You have been logged out.")
#     else:
#         messages.error(request,logout_user, "You are not logged in.")
#     return redirect('home')  # Redirect to the homepage
# def logout(request):
#     try:
#         user_id = request.session.pop('user_id')
#         del request.session['user_id']  # Remove user_id from session
#         del request.session['username']  # Optional: Remove username
#         messages.success(request, "You have been logged out successfully!")
#     except KeyError:
#         # If 'user_id' or 'username' is not in the session, handle it gracefully
#         pass
#     return redirect('index')  # Redirect to login page or homepage
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             # Retrieve the user by username
#             user = Register.objects.get(username=username)

#             # Check if the password matches
#             if check_password(password, user.password):
#                 # Check if the user is 'admin1' for admin login
#                 if username == 'admin1':
#                     messages.success(request, 'Admin login successful')
#                     return redirect('admin_dashboard')  # Redirect to the admin dashboard
                
#                 # Regular user login
#                 request.session['user_id'] = user.id  # Save user ID in the session
#                 request.session['username'] = user.username  # Save username for convenience
#                 messages.success(request, f"Welcome, {user.username}!")
#                 request.session.save()
#                 return redirect('index')  # Redirect to the user's homepage
#             else:
#                 # Incorrect password
#                 messages.error(request, 'Incorrect password. Please try again.')
#                 return redirect('login')

#         except Register.DoesNotExist:
#             # User does not exist
#             messages.error(request, 'Username does not exist. Please register first.')
#             return redirect('login')

#     return render(request, 'users/login.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
       
                 # Check if the user is 'admin1' for admin login
        if username == 'admin1':
            messages.success(request, 'Admin login successful')
            return redirect('admin_dashboard')  # Redirect to the admin dashboard

        if user is not None:
            auth_login(request, user)
            
            # Redirect to 'next' URL if provided, else to LOGIN_REDIRECT_URL
            next_url = request.GET.get('next', '/')  # Default to '/'
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')  # Redirect back to login page if failed

    return render(request, 'registration/login.html')
# def logout(request):
#     try:
#         # Clear session data
#         if 'user_id' in request.session:
#             del request.session['user_id']  # Remove user_id from session
#         if 'username' in request.session:
#             del request.session['username']  # Optional: Remove username
#         messages.success(request, "You have been logged out successfully!")
#     except KeyError:
#         # If 'user_id' or 'username' is not in the session, handle it gracefully
#         pass
    
#     return redirect('index')  # Redirect to the login page after logout
def logout(request):
    auth_logout(request)  # Properly log out the user
    messages.success(request, "You have been logged out successfully!")
    return redirect('index')



# @login_required
# def account(request):
#     user = request.user  # Get the logged-in user

#     # Fetch user details
#     user_details = get_object_or_404(Register, id=user.id)

#     # Fetch user's addresses
#     addresses = Address.objects.filter(user=user)  # Assuming Address model has a ForeignKey to Register
#     states = State.objects.all()
#     districts = District.objects.all()


#     return render(request, 'registration/account.html', {
#         'user_details': user_details,
#         'addresses': addresses,
#         'states': states,
#         'districts': districts
#     })

@login_required
def account(request):
    user = request.user
    user_details = get_object_or_404(Register, id=user.id)
    addresses = Address.objects.filter(user=user)
    states = State.objects.all().order_by('name')

    if request.method == "POST":
        # Handle address update
        address_id = request.POST.get("address_id")
        address = get_object_or_404(Address, id=address_id, user=user)
        
        # Update address fields
        address.first_name = request.POST.get("first_name")
        address.last_name = request.POST.get("last_name")
        address.email = request.POST.get("email")
        address.phone = request.POST.get("phone")
        address.address = request.POST.get("address")
        address.address2 = request.POST.get("address2")
        
        # Update state and district if changed
        state_id = request.POST.get("state")
        district_id = request.POST.get("district")
        if state_id:
            address.state = get_object_or_404(State, id=state_id)
        if district_id:
            address.district = get_object_or_404(District, id=district_id)
            
        address.pin = request.POST.get("pin")
        address.save()
        
        messages.success(request, "Address updated successfully!")
        return redirect('update_address')

    return render(request, 'registration/update_address.html', {
        'user_details': user_details,
        'addresses': addresses,
        'states': states,
    })