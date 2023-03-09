import datetime
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


# Create your views here.

def store(request):
    # temporary code
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
        cardItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cardItems = order['get_cart_items']
    # temporary code

    products = Product.objects.all()
    context = {'products': products, 'cardItems': cardItems}
    return render(request, 'store/index.html', context)


def catalog(request):
    # temporary code
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
        cardItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cardItems = order['get_cart_items']
    # temporary code

    products = Product.objects.all()
    context = {'products': products, 'cardItems': cardItems}
    return render(request, 'store/shop.html', context)


def blog(request):
    # temporary code
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
        cardItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cardItems = order['get_cart_items']
    # temporary code

    context = {}
    return render(request, 'store/blog.html', context)


def about(request):
    # temporary code
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
        cardItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cardItems = order['get_cart_items']
    # temporary code

    context = {}
    return render(request, 'store/about.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def login_page(request):
    context = {}
    return render(request, 'store/login.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)


def detail(request):
    context = {}
    return render(request, 'store/detail.html', context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(action)
    print(productId)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,
                                                 complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,
                                                         product=product)
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0 or action == 'delete_item':
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                citi=data['shipping']['citi'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )

    else:
        print('User is not logged in')
    return JsonResponse('Payment complete!', safe=False)
