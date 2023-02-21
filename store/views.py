from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


# def store(request):
#     context = {}
#     return render(request, "Store.html", context)
#
#
# def cart(request):
#     context = {}
#     return render(request, "Cart.html", context)
#
#
# def checkout(request):
#     context = {}
#     return render(request, "Checkout.html", context)


def drinks(request, drink_name):
    drink = {
        '1' : 'type of coffee',
        '2' : 'type of hot beverage',
        '3': 'type of refreshment'
    }
    # type = drink["drink_name"]

    return HttpResponse(f"<h2>{drink_name}</h2> " )
