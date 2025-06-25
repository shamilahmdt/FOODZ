from django.contrib import admin

from customer.models import Customer,Address,Cart,CartBill,Order,OrderItem,Offer


admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartBill)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Offer)
