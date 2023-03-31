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
    path('detail/', views.detail, name='detail'),
    path('update_item/', views.update_item, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),

]
