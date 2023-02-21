
from django.urls import path

from store import views

urlpatterns = [
    # path('',views.store,name="store" ),
    # path('cart/',views.cart,name="cart" ),
    # path('checkout/',views.checkout,name="checkout" ),
    # path('',views.index,name="checkout" ),
    path('drinks/<int:drink_name>', views.drinks, name="drink_name"),


]
