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
            "imagee":forms.widgets.FileInput(attrs={"class":"form-control"})
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
        fields = ["name", "image"]

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
