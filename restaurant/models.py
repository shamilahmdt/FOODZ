from django.db import models
from customer.models import *



class StoreCategory(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='category')

    class Meta:
        db_table = 'restaurant_store_categoy'
        verbose_name = 'store category'
        verbose_name_plural = 'store categories'
        ordering = ['-id']

    def __str__(self):
        return self.name
    

class Store(models.Model):
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=300)
    category = models.ManyToManyField(StoreCategory)
    image = models.FileField(upload_to='store')
    rating = models.FloatField()
    time = models.IntegerField()
    offer = models.CharField(max_length=255)


    class Meta:
        db_table = 'restaurant_store'
        verbose_name = 'store'
        verbose_name_plural = 'stores'
        ordering = ['-id']


    def __str__(self):
        return self.name
    


class Slider(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='slide')
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


    class Meta:
        db_table = 'restaurant_slider'
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'
        ordering = ['-id']


    def __str__(self):
        return self.name
    


class FoodCategory(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        db_table = 'food_category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['-id']


    def __str__(self):
        return self.name
    


class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    is_veg = models.BooleanField(default=False)
    price = models.IntegerField()
    image = models.FileField(upload_to='fooditem')
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='fooditems')
    restaurant = models.ForeignKey(Store, on_delete=models.CASCADE)


    class Meta:
        db_table = 'food_item'
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ['-id']


    def __str__(self):
        return self.name
    
class StoreManager(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'restaurant_store_manager'
        verbose_name = 'store manager'
        verbose_name_plural = 'store managers'
        ordering = ['-id']

    def _str_(self):
        return f"{self.user.email} - {self.store.name}"