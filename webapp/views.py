from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm
# from django.http import HttpResponse

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

@unauthenticated_user
def registerPage(request):
    
    # form = CreateUserForm()
	# if request.method == 'POST':
	# 	form = CreateUserForm(request.POST)
	# 	if form.is_valid():
	# 		user = form.save()
	# 		username = form.cleaned_data.get('username')

	# 		group = Group.objects.get(name='customer')
	# 		user.groups.add(group)

	# 		messages.success(request, 'Account was created for ' + username)

	# 		return redirect('login')

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
   
			# group = Group.objects.get(name='customer')
			# user.groups.add(group)
   
			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
			

	context = {'form':form}
	
	return render(request, 'signup.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
    
   return render(request, 'home.html', {})

@login_required(login_url='login')
def main(request):
   # return HttpResponse('OPOOOOR')
   return render(request, 'main.html', {})

@login_required(login_url='login')
def dashboard(request):
   # return HttpResponse('OPOOOOR')
	orders = Order.objects.all()
	products = Product.objects.all()

	total_orders = orders.count()
	delivered = orders.filter(order_status='Delivered').count()
	pending = orders.filter(order_status='Pending').count()

	context = {'orders':orders,
	'total_orders':total_orders, 'products':products,
 	'delivered':delivered, 'pending':pending}

	return render(request, 'dashboard.html', context)
	
#    return render(request, 'dashboard.html', {})

@login_required(login_url='login')
def about(request):
   # return HttpResponse('OPOOOOR')
   return render(request, 'about.html', {})

@login_required(login_url='login')
def services(request):
   # return HttpResponse('OPOOOOR')
   return render(request, 'services.html', {})

@login_required(login_url='login')
def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = { 'form':form }
	return render(request, 'createorder.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'createorder.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'order':order}
	return render(request, 'delete.html', context)



# @login_required(login_url='login')
# def home(request):
# 	orders = Order.objects.all()
# 	customers = Customer.objects.all()

# 	total_customers = customers.count()

# 	total_orders = orders.count()
# 	delivered = orders.filter(status='Delivered').count()
# 	pending = orders.filter(status='Pending').count()

# 	context = {'orders':orders, 'customers':customers,
# 	'total_orders':total_orders,'delivered':delivered,
# 	'pending':pending }

# 	return render(request, 'accounts/dashboard.html', context)

# @login_required(login_url='login')
# def products(request):
# 	products = Product.objects.all()

# 	return render(request, 'accounts/products.html', {'products':products})

# @login_required(login_url='login')
# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)

# 	orders = customer.order_set.all()
# 	order_count = orders.count()

# 	myFilter = OrderFilter(request.GET, queryset=orders)
# 	orders = myFilter.qs 

# 	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
# 	'myFilter':myFilter}
# 	return render(request, 'accounts/customer.html',context)

# @login_required(login_url='login')
# def createOrder(request, pk):
# 	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
# 	customer = Customer.objects.get(id=pk)
# 	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
# 	#form = OrderForm(initial={'customer':customer})
# 	if request.method == 'POST':
# 		#print('Printing POST:', request.POST)
# 		form = OrderForm(request.POST)
# 		formset = OrderFormSet(request.POST, instance=customer)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect('/')

# 	context = {'form':formset}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def updateOrder(request, pk):

# 	order = Order.objects.get(id=pk)
# 	form = OrderForm(instance=order)

# 	if request.method == 'POST':
# 		form = OrderForm(request.POST, instance=order)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context = {'form':form}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def deleteOrder(request, pk):
# 	order = Order.objects.get(id=pk)
# 	if request.method == "POST":
# 		order.delete()
# 		return redirect('/')

# 	context = {'item':order}
# 	return render(request, 'accounts/delete.html', context)