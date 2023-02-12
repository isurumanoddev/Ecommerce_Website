from django.shortcuts import render


# Create your views here.


def store(request):
    context = {}
    return render(request, "Store.html", context)


def cart(request):
    context = {}
    return render(request, "Cart.html", context)


def checkout(request):
    context = {}
    return render(request, "Checkout.html", context)
