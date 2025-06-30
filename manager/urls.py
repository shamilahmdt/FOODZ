from django.urls import path
from manager import views

app_name = "manager"


urlpatterns = [
   path('', views.dashboard, name="dashboard"),
   path('store_category/', views.store_category, name="store_category"),
   path('store_category/create', views.store_category_create, name="store_category_create"),
   path('store_category/update/<int:id>/', views.store_category_update, name="store_category_update"),
   path('store_category/delete/<int:id>/', views.store_category_delete, name="store_category_delete"),

   path('orders/', views.orders, name="orders"),
   
   path('order/<int:id>/', views.order, name="order"),
   path('order/assign/<int:id>/', views.order_assign, name="order_assign"),
   path('order/accept/<int:id>/', views.order_accept, name="order_accept"),
   path('order/reject/<int:id>/', views.order_reject, name="order_reject"),
   path('order/prepared/<int:id>/', views.order_prepared, name="order_prepared"),
   path('order/picked/<int:id>/', views.order_picked, name="order_picked"),
   path('order/completed/<int:id>/', views.order_completed, name="order_completed"),

   path('store/', views.store, name="store"),
   path('store/create', views.store_create, name="store_create"),
   path('store/update/<int:id>/', views.store_update, name="store_update"),
   path('store/delete/<int:id>/', views.store_delete, name="store_delete"),

   path('slider/', views.slider, name="slider"),
   path('slider/create', views.slider_create, name="slider_create"),
   path('slider/update/<int:id>/', views.slider_update, name="slider_update"),
   path('slider/delete/<int:id>/', views.slider_delete, name="slider_delete"),

   path('food_item/', views.food_item, name="food_item"),
   path('food_item/create', views.food_item_create, name="food_item_create"),
   path('food_item/update/<int:id>/', views.food_item_update, name="food_item_update"),
   path('food_item/delete/<int:id>/', views.food_item_delete, name="food_item_delete"),

   path('food_category/', views.food_category, name="food_category"),
   path('food_category/create', views.food_category_create, name="food_category_create"),
   path('food_category/update/<int:id>/', views.food_category_update, name="food_category_update"),
   path('food_category/delete/<int:id>/', views.food_category_delete, name="food_category_delete"),

   path('cart/', views.cart, name="cart"),
   path('cart/create', views.cart_create, name="cart_create"),
   path('cart/update/<int:id>/', views.cart_update, name="cart_update"),
   path('cart/delete/<int:id>/', views.cart_delete, name="cart_delete"),

   path('customer/', views.customer, name="customer"),
   path('customer/create', views.customer_create, name="customer_create"),
   path('customer/update/<int:id>/', views.customer_update, name="customer_update"),
   path('customer/delete/<int:id>/', views.customer_delete, name="customer_delete"),

   path('address/', views.address, name="address"),
   path('address/create', views.address_create, name="address_create"),
   path('address/update/<int:id>/', views.address_update, name="address_update"),
   path('address/delete/<int:id>/', views.address_delete, name="address_delete"),

   path('cart/', views.cart, name="cart"),
   path('cart/create', views.cart_create, name="cart_create"),
   path('cart/update/<int:id>/', views.cart_update, name="cart_update"),
   path('cart/delete/<int:id>/', views.cart_delete, name="cart_delete"),

   path('cartbill/', views.cartbill, name="cartbill"),
   path('cartbill/create', views.cartbill_create, name="cartbill_create"),
   path('cartbill/update/<int:id>/', views.cartbill_update, name="cartbill_update"),
   path('cartbill/delete/<int:id>/', views.cartbill_delete, name="cartbill_delete"),

   path('full_orders/', views.full_orders, name="full_orders"),
   path('full_orders/create', views.full_orders_create, name="full_orders_create"),
   path('full_orders/update/<int:id>/', views.full_orders_update, name="full_orders_update"),
   path('full_orders/delete/<int:id>/', views.full_orders_delete, name="full_orders_delete"),

   path('order_item/', views.order_item, name="order_item"),
   path('order_item/create', views.order_item_create, name="order_item_create"),
   path('order_item/update/<int:id>/', views.order_item_update, name="order_item_update"),
   path('order_item/delete/<int:id>/', views.order_item_delete, name="order_item_delete"),

   path('offer/', views.offer, name="offer"),
   path('offer/create', views.offer_create, name="offer_create"),
   path('offer/update/<int:id>/', views.offer_update, name="offer_update"),
   path('offer/delete/<int:id>/', views.offer_delete, name="offer_delete"),
]