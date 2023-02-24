from django.shortcuts import render


# Create your views here.

def store(request):
    context = {}
    return render(request, 'store/index.html', context)


def catalog(request):
    context = {}
    return render(request, 'store/shop.html', context)


def blog(request):
    context = {}
    return render(request, 'store/blog.html', context)


def about(request):
    context = {}
    return render(request, 'store/about.html', context)


def contact(request):
    context = {}
    return render(request, 'store/contact.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def login_page(request):
    context = {}
    return render(request, 'store/login.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
