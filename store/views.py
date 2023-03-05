from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from store.models import Product, Order, OrderItem, ShippingAddress
import datetime


def store(request):
    products = Product.objects.all()

    context = {"products": products, }
    return render(request, "Store.html", context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}

    context = {"items": items, "order": order}
    return render(request, "Cart.html", context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False, )
        items = order.orderitem_set.all()
        create = items.create()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0, "shipping": False}

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
    product_id = data["productId"]
    action = data["action"]
    product = Product.objects.get(id=product_id)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(complete=False, customer=customer)

    orderItem, created = OrderItem.objects.get_or_create(product=product, order=order)

    if action == "add":
        orderItem.quantity += 1
    elif action == "remove":
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("item was added", safe=False)


def delete_items(request, pk):
    order = Order.objects.get(id=pk)
    cart_items = order.orderitem_set.all()
    if request.method == "POST":
        if cart_items is not None:
            cart_items.delete()
            order.delete()
        return redirect("store")

    context = {"order": order}
    return render(request, "delete.html", context)


def process_order(request):
    form_data = json.loads(request.body)

    transaction_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(form_data["userFormData"]["total"])
        order.transaction_id = transaction_id
        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=form_data["shippingInfo"]["address"],
                city=form_data["shippingInfo"]["city"],
                state=form_data["shippingInfo"]["state"],
                zip_code=form_data["shippingInfo"]["zipcode"],

            )

        else:
            print("user not log in")
        return JsonResponse("payment complete......", safe=False)
