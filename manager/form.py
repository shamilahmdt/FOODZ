from django import forms

from users.models import User
from customer.models import *
from restaurant.models import *


class StoreCategoryForm(forms.ModelForm):
    class Meta:
        model = StoreCategory
        fields = ["name", "image"]

        widgets = {
            "name":forms.widgets.TextInput(attrs={"class":"form-control","placeholder":"Category name"}),
            "image":forms.widgets.FileInput(attrs={"class":"form-control"})
        }

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ["name", "tagline", "category", "image", "rating", "time", "offer"]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Store Name'}),
            'tagline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Store Tagline'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': 0, 'max': 5}),
            'time': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Delivery Time (mins)'}),
            'offer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Offer Details'})
        }

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ["name", "image",'store']

        widgets = {
            "name":forms.widgets.TextInput(attrs={"class":"form-control","placeholder":"Slider name"}),
            "image":forms.widgets.FileInput(attrs={"class":"form-control"}),
            'store': forms.Select(attrs={'class': 'form-control'}),
        }

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = ["name",'is_veg','price','image','category', "restaurant"]

        widgets = {
            "name" : forms.widgets.TextInput(attrs={"class":"form-control","placeholder":"FoodCategory name"}),
            'is_veg': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            "restaurant" : forms.Select(attrs={"class":"form-control"}),
        }

class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ["name", "restaurant"]

        widgets = {
            "name" : forms.widgets.TextInput(attrs={"class":"form-control","placeholder":"FoodCategory name"}),
            "restaurant" : forms.Select(attrs={"class":"form-control"})
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['user']

        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "customer", "address", "address_type", "landmark",
            "latitude", "longitude", "appartment", "is_selected"
        ]
        
        widgets = {
            "customer": forms.Select(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Full address"}),
            "address_type": forms.TextInput(attrs={"class": "form-control", "placeholder": "Home / Work / Other"}),
            "landmark": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nearby landmark"}),
            "latitude": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Latitude"}),
            "longitude": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Longitude"}),
            "appartment": forms.TextInput(attrs={"class": "form-control", "placeholder": "Flat / Apartment name"}),
            "is_selected": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ["customer", "product", "qty", "store", "amnt"]

        widgets = {
            "customer": forms.Select(attrs={"class": "form-control"}),
            "product": forms.Select(attrs={"class": "form-control"}),
            "qty": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Quantity"}),
            "store": forms.Select(attrs={"class": "form-control"}),
            "amnt": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Amount"}),
        }

class CartBillForm(forms.ModelForm):
    class Meta:
        model = CartBill
        fields = ['customer', 'offer_amnt', 'delivery_charge', 'coupen_code']

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'offer_amnt': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Offer Amount'}),
            'delivery_charge': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Delivery Charge'}),
            'coupen_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coupon Code'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "customer", "order_id", "address", "status",
            "sub_total", "total", "store", "delivery_charge"
        ]

        widgets = {
            "customer": forms.Select(attrs={"class": "form-control"}),
            "order_id": forms.TextInput(attrs={"class": "form-control", "placeholder": "Order ID"}),
            "address": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "sub_total": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Subtotal"}),
            "total": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Total"}),
            "store": forms.Select(attrs={"class": "form-control"}),
            "delivery_charge": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Delivery Charge"}),
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['customer', 'order', 'product', 'qty', 'store', 'amnt']

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'qty': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'store': forms.Select(attrs={'class': 'form-control'}),
            'amnt': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['coupen_code', 'description', 'offer', 'is_percentage']

        widgets = {
            'coupen_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Coupon Code'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Short Description'}),
            'offer': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Offer Value'}),
            'is_percentage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }        