from django.db import models

from users.models import User

from restaurant.models import Store, FoodItem

ORDER_STATUS_CHOICES=(
    ('PL', 'PL'),
    ('AC', 'AC'),
    ('PR', 'PR'),
    ('DI', 'DI'),
    ('CA', 'CA'),

)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'customer_table'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
        ordering = ['-id']


    def _str_(self):
        return self.user.email


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.TextField()
    address_type = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    latitude = models.FloatField(null=True, blank=True) 
    longitude = models.FloatField(null=True, blank=True)    
    appartment = models.CharField(max_length=200)
    is_selected = models.BooleanField(default=False)
    



    class Meta:
        db_table = 'customer_address'
        verbose_name = 'address'
        verbose_name_plural = 'addresses'
        ordering = ['-id']


    def _str_(self):
        return self.customer



class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    qty = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    amnt = models.FloatField()

    class Meta:
        db_table = 'customer_cart'
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
        ordering = ['-id']


    def _str_(self):
        return self.product.name    
    

class CartBill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    offer_amnt = models.FloatField(default=0, null=True, blank=True)
    delivery_charge = models.FloatField(default=0)
    coupen_code = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'customer_cartbill'
        verbose_name = 'cart_bill'
        verbose_name_plural = 'carts_bills'
        ordering = ['-id']


    def _str_(self):
        return self.customer.user.email
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=ORDER_STATUS_CHOICES)
    sub_total = models.FloatField()
    total = models.FloatField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    delivery_charge = models.IntegerField(default=0)

    class Meta:
        db_table = 'customer_order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ['-id']


    def _str_(self):
        return self.customer.user.email
    
class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    qty = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    amnt = models.FloatField()

    class Meta:
        db_table = 'customer_order_item'
        verbose_name = 'order_item'
        verbose_name_plural = 'order_items  '
        ordering = ['-id']


    def _str_(self):
        return self.customer.user.email
    
class Offer(models.Model):
    coupen_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    offer = models.IntegerField()
    is_percentage = models.BooleanField(default=False) 

    class Meta:
        db_table = 'customer_offer'
        verbose_name = 'offer'
        verbose_name_plural = 'offers  '
        ordering = ['-id']


    def _str_(self):
        return self.coupon_code