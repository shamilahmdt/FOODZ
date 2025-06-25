from django.urls import path
from manager import views

app_name = "manager"


urlpatterns = [
   path('', views.dashboard, name="dashboard"),
   path('store_category/', views.store_category, name="store_category"),
   path('store_category/create', views.store_category_create, name="store_category_create"),
   path('store_category/update/<int:id>/', views.store_category_update, name="store_category_update"),
   path('store_category/delete/<int:id>/', views.store_category_delete, name="store_category_delete"),

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

   path('food_category/', views.food_category, name="food_category"),
   path('food_category/create', views.food_category_create, name="food_category_create"),
   path('food_category/update/<int:id>/', views.food_category_update, name="food_category_update"),
   path('food_category/delete/<int:id>/', views.food_category_delete, name="food_category_delete"),

   
]