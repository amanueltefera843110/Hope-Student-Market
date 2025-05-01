from django.shortcuts import render, redirect

from .models import Product, Category, Profile

from django.contrib.auth import authenticate , login , logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from .forms import SignUpForm,UpdateUserForm,ChangePasswordForm,UserInfoForm
from payment.forms import ShippingForm
from payment.models import ShipingAddress
from django import forms
from django.db.models import Q
import json
from cart.cart import Cart
from .forms import ProductForm
from .models import Product


def search(request):
	# Determine if they filled out the form
	if request.method == "POST":
		searched = request.POST['searched']
		# Query The Products DB Model
		searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
		# Test for null
		if not searched:
			messages.success(request, "That Product Does Not Exist...Please try Again.")
			return render(request, "search.html", {})
		else:
			return render(request, "search.html", {'searched':searched})
	else:
		return render(request, "search.html", {})	

	
def update_info(request):
	if request.user.is_authenticated:
		# Get Current User
		current_user = Profile.objects.get(user__id=request.user.id)
		# Get Current User's Shipping Info
		shipping_user = ShipingAddress.objects.get(user__id=request.user.id)
		
		# Get original User Form
		form = UserInfoForm(request.POST or None, instance=current_user)
		# Get User's Shipping Form
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)		
		if form.is_valid() or shipping_form.is_valid():
			# Save original form
			form.save()
			# Save shipping form
			shipping_form.save()

			messages.success(request, "Your Info Has Been Updated!!")
			return redirect('home')
		return render(request, "update_info.html", {'form':form, 'shipping_form':shipping_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')



def update_password(request):
	if request.user.is_authenticated:
		current_users = request.user
		if request.method == 'POST':
			form = ChangePasswordForm(current_users, request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, ("User PasswordHhas Been Updated"))
				login(request, current_users)
				return redirect('update_user')

			else:
				for error in list(form.errors.values()):
					messages.error(request,error)
					return redirect('update_password')
				


		else:
			form = ChangePasswordForm(current_users)
			return render(request, 'update_password.html', {"form":form})

	else:
		messages.success(request, ("Must Login to view the page"))
		return redirect('home')

	
def update_user(request):
	if request.user.is_authenticated:
		current_users = User.objects.get(id=request.user.id)
		user_form = UpdateUserForm(request.POST or None, instance=current_users)# if click on button update or keep same info
		if user_form.is_valid():
			user_form.save()
			login(request,current_users)
			messages.success(request, ("User has been Updated"))
			return redirect('home')
		return render(request, 'update_user.html', {'user_form': user_form})

	else:
		messages.success(request, ("You must be login go get into the websit"))
		return redirect('home')

def category_summary(request):

	categories = Category.objects.all()

	return render(request, 'category_summary.html', {"categories": categories})

# Create your views here.
def category (request,foo):
	# change the url form having - to having just a space
	foo = foo.replace('-',' ')
	# get the category form the database
	try:
		#look up the category and get it form the database of Category with the name
		category = Category.objects.get(name=foo)
		# get the products in that category
		products = Product.objects.filter(category= category)
		return render(request, 'category.html',{'products': products,'category':category})
	except:
		messages.success(request, ("Sorry this in't a category we have "))
		return redirect('home')

def home(request):
	products = Product.objects.all()
	return render(request, 'home.html', {'products':products})
def about(request):
		return render(request, 'about.html', {})
def login_user(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username= username , password = password)
		if user is not None:
			login(request , user)

			# shoping cart 
			current_user = Profile.objects.get(user__id=request.user.id)
			# get the saved cart form data base
			save_cart = current_user.old_cart
			# make the string into a dec
			if save_cart:
				#use json to change it
				converted_cart = json.loads(save_cart)
				#add the loaded cart dictionary to our session
				#get the cart
				cart= Cart(request)
				# loop to add the item form data base
				for key,values in converted_cart.items():
					cart.db_add(product = key, quantity= values)







			messages.success(request, ("You have been logged IN!!"))
			return redirect('home')
		else:
			messages.success(request, ("WRONG ERROR "))
			return redirect('login')
	else:
		return render(request,'login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, ("You have been logged out!!"))
	return redirect('home')

def register_user(request):
	form = SignUpForm()
	if request.method == "POST": # post the info to the back end
		form = SignUpForm(request.POST) # get it form the baackend
		if form.is_valid():# check if evething is there
			form.save()#save it if its good
			username =form.cleaned_data['username']#getusername
			password =form.cleaned_data['password1']#getpassword
			useremail = form.cleaned_data['email']
			# log in user
			send_mail(
                subject="Welcome to Our Site!",
                message="Thanks for registering on our site. We’re glad to have you!",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[useremail],
                fail_silently=False,  # set to True in production to avoid errors crashing the app
            )

			user = authenticate(username= username , password= password)
			login(request, user)
			messages.success(request, ("You have Register successfully, Please fill out your User info"))
			return  redirect('update_info')
		else:
			messages.success(request, ("Somthing went wrong in Username or password, Pls try again"))
			return  redirect('register')

	return render(request, 'register.html', {"form":form})
def product(request,pk):
	product = Product.objects.get(id=pk)
	return render(request, 'product.html', {'product':product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the product list page
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {'form': form})





