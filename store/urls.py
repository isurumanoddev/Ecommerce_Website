from django.urls import path

from store import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('user_login/', views.user_login, name="login"),
    path('user_logout/', views.user_logout, name="logout"),
    path('user_register/', views.user_register, name="register"),

    path('clear_cart/<str:pk>', views.clear_cart, name="clear-cart"),

    path('update_cart/', views.update_cart, name="update-cart"),

    path('process_order/', views.process_order, name="process-order"),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
