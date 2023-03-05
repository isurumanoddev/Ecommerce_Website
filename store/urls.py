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

    path('delete_items/<str:pk>', views.delete_items, name="delete-items"),

    path('update_item/', views.update_item, name="update-item"),

    path('process_order/', views.process_order, name="process-order"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
