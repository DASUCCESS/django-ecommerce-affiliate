from django.urls import path, include
from . import views

urlpatterns = [
    
    path('login/', views.loginPage, name="login"),  
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
 
    path('', views.home, name='home' ),
    path('main', views.main, name='main' ),
    path('dashboard', views.dashboard, name='dashboard' ),
    path('about', views.about, name='about' ),
    path('services', views.services, name='services' ),
    path('createorder/', views.createOrder, name="createorder"),
    path('updateorder/<str:pk>/', views.updateOrder, name="updateorder"),
    path('deleteorder/<str:pk>/', views.deleteOrder, name="deleteorder"),
	
	
    

    # path('', views.home, name="home"),
    # path('products/', views.products, name='products'),
    # path('customer/<str:pk_test>/', views.customer, name="customer"),

    # path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    # path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
