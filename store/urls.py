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

    path('clear_all/', views.clear_all, name="clear_all"),

    path('update_item/', views.update_item, name="update-item"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
