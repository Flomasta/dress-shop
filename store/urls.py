from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('shop/', views.catalog, name='catalog'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('login-page/', views.login_page, name='login-page'),
    path('checkout/', views.checkout, name='checkout'),

]
