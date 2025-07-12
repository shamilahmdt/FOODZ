from django.urls import path
from api.v1.customer import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),

    path('address/', views.address, name='address'),
    path('address/add/', views.address_add, name='address_add'),
    path('address/update/<int:id>', views.address_update, name='address_update'),
    path('address/delete/<int:id>', views.address_delete, name='address_delete'),

]