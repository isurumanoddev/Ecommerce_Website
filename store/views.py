from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

from store.models import Product


def store(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "Store.html", context)


def cart(request):
    context = {}
    return render(request, "Cart.html", context)


def checkout(request):
    context = {}
    return render(request, "Checkout.html", context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")

        try:
            User.objects.get(username=username)
        except:
            print("user not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect("store")
    context = {}
    return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return redirect("store")
