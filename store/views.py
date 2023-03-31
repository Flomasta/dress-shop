import datetime
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from .utils import cookieCart, cartData, guestOrder
from django.views.decorators.csrf import csrf_exempt
import stripe
from settings.settings import STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY

stripe.api_key = STRIPE_SECRET_KEY


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/index.html', context)


def catalog(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/shop.html', context)


def blog(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    return render(request, 'store/blog.html', context)


def about(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    return render(request, 'store/about.html', context)


def contact(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {'cartItems': cartItems}
    return render(request, 'store/contact.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def login_page(request):
    context = {}
    return render(request, 'store/login.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    price_for_pp = order.get_cart_total * 100
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'total_amount': price_for_pp}
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

    else:
        customer, order = guestOrder(request, data)
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
    return JsonResponse('Payment complete!', safe=False)


YOUR_DOMAIN = 'http://127.0.0.1:8000'


def create_checkout_session(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST['stripeToken']
        amount = int(request.POST['amount'])

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                description='Example charge',
                source=token,
            )
        except stripe.error.CardError as e:
            return render(request, 'charge.html', {'error': e})

        return render(request, 'charge.html', {'charge': charge, 'publishable_key': stripe.api_key})
    else:
        return render(request, 'charge.html', {'publishable_key': stripe.api_key})
