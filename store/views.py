from django.shortcuts import render
from django.http import HttpResponse


def store(request):
    context = {}
    return render(request, "Checkout.html", context)


def cart(request):
    context = {}
    return render(request, "Cart.html", context)


def checkout(request):
    context = {}
    return render(request, "Checkout.html", context)
