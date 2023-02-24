from django.shortcuts import render
from django.http import HttpResponse

from store.models import Product


def store(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request, "Store.html", context)


def cart(request):
    context = {}
    return render(request, "Cart.html", context)


def checkout(request):
    context = {}
    return render(request, "Checkout.html", context)
