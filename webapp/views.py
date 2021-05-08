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
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
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
