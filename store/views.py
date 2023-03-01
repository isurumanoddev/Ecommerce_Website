from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from store.models import Product, Order, OrderItem


def store(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "Store.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

    context = {"items": items, "order": order}
    return render(request, "Cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

    context = {"items": items, "order": order}
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
            login(request, user)
            return redirect("store")
    context = {}
    return render(request, "login.html", context)


def user_logout(request):
    logout(request)
    return redirect("store")


def update_item(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    print("productId :", productId, "action :", action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(product=product, order=order)

    if action == "add":
        orderItem.quantity += 1
    elif action == "remove":
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse("Item was added", safe=False)
