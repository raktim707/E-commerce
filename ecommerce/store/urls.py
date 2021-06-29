from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns=[
    path('', views.store, name='store'),
    path('process_order/', views.processOrder, name="process_order"),
    path('update_item/', views.updateCart, name='update_item'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('product_detail/<int:id>', views.productDetail, name="product_detail"),
]