from django.shortcuts import get_object_or_404, render,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from users.models import User
from customer.models import *
from restaurant.models import *

from .form import *

def dashboard(request):
    instances = Order.objects.all()
    context={
        "instances" : instances,
    }
    return render(request, 'manager/index.html', context=context)    


@login_required(login_url='/manager/login')
def store_category(request):
    instances = StoreCategory.objects.all()

    context={
        "title" : "Store Categories | Dashboard",
        "sub_title" : "Store Categories",
        "name" : "Store Categories",
        "instances" : instances,

    }
    return render(request, 'manager/store_category.html', context=context)    

def store_category_create(request):
    if request.method == "POST":
        form = StoreCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:store_category'))
        
        else:
            pass
    else:
        form = StoreCategoryForm()
        context={
            "title" : "Store Categories | Dashboard",
            "sub_title" : "Store Categories",
            "name" : "Create Store Categories",
            "form" : form,

        }
        return render(request, 'manager/update_store_category.html', context=context)

def store_category_update(request, id):
    instance = get_object_or_404(StoreCategory,id=id)
    if request.method == "POST":
        form = StoreCategoryForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:store_category'))
        else:
            pass
    else:
        form = StoreCategoryForm(instance=instance)
        context={
            "title" : "Store Categories | Dashboard",
            "sub_title" : "Store Categories",
            "name" : "Create Store Categories",
            "form" : form,

        }
        return render(request, 'manager/update_store_category.html', context=context) 
                    
def store_category_delete(request, id):
    instance = get_object_or_404(StoreCategory,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:store_category'))

def order(request,id):
    pass

def order_assign(request,id):
    pass

def order_accept(request,id):
    order = Order.objects.get(id=id)

    order.status = 'AC'
    order.save()
    return HttpResponseRedirect(reverse('manager:dashboard'))



def order_reject(request,id):
    order = Order.objects.get(id=id)

    order.status = 'CA'
    order.save()
    return HttpResponseRedirect(reverse('manager:dashboard'))

def order_prepared(request,id):
    order = Order.objects.get(id=id)

    order.status = 'PR'
    order.save()
    return HttpResponseRedirect(reverse('manager:dashboard'))

def order_picked(request,id):
    order = Order.objects.get(id=id)

    order.status = 'DI'
    order.save()
    return HttpResponseRedirect(reverse('manager:dashboard'))

def order_completed(request,id):
    order = Order.objects.get(id=id)

    order.status = 'CO'
    order.save()
    return HttpResponseRedirect(reverse('manager:dashboard'))

def store(request):
    instances = Store.objects.all()

    context={
        "title" : "Store | Dashboard",
        "sub_title" : "Stores",
        "name" : "Store",
        "instances" : instances,

    }
    return render(request, 'manager/store.html', context=context)

def store_create(request):
    if request.method == "POST":
        form = StoreForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:store'))
        
        else:
            pass
    else:
        form = StoreForm()
        context={
            "title" : "Store | Dashboard",
            "sub_title" : "Stores",
            "name" : "Store",
            "form" : form,

        }
        return render(request, 'manager/update_store.html', context=context)

def store_update(request, id):
    instance = get_object_or_404(Store,id=id)
    if request.method == "POST":
        form = StoreForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:store'))
        else:
            pass
    else:
        form = StoreForm(instance=instance)
        context={
            "title" : "Store | Dashboard",
            "sub_title" : "Stores",
            "name" : "Store",
            "form" : form,

        }
        return render(request, 'manager/update_store.html', context=context) 
                    
def store_delete(request, id):
    instance = get_object_or_404(Store,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:store'))


def slider(request):
    instances = Slider.objects.all()

    context={
        "title" : "slider | Dashboard",
        "sub_title" : "sliders",
        "name" : "slider",
        "instances" : instances,

    }
    return render(request, 'manager/slider.html', context=context)

def slider_create(request):
    if request.method == "POST":
        form = SliderForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:slider'))
        
        else:
            pass
    else:
        form = SliderForm()
        context={
            "title" : "slider | Dashboard",
            "sub_title" : "sliders",
            "name" : "slider",
            "form" : form,

        }
        return render(request, 'manager/update_slider.html', context=context)

def slider_update(request, id):
    instance = get_object_or_404(Slider,id=id)
    if request.method == "POST":
        form = SliderForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:slider'))
        else:
            pass
    else:
        form = SliderForm(instance=instance)
        context={
            "title" : "slider | Dashboard",
            "sub_title" : "sliders",
            "name" : "slider",
            "form" : form,

        }
        return render(request, 'manager/update_slider.html', context=context) 
                    
def slider_delete(request, id):
    instance = get_object_or_404(Slider,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:slider'))

def food_category(request):
    instances = food_category.objects.all()

    context={
        "title" : "food_category | Dashboard",
        "sub_title" : "food_categorys",
        "name" : "food_category",
        "instances" : instances,

    }
    return render(request, 'manager/food_category.html', context=context)

def food_category_create(request):
    if request.method == "POST":
        form = FoodCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:food_category'))
        
        else:
            pass
    else:
        form = FoodCategoryForm()
        context={
            "title" : "food_category | Dashboard",
            "sub_title" : "food_categorys",
            "name" : "food_category",
            "form" : form,

        }
        return render(request, 'manager/update_food_category.html', context=context)

def food_category_update(request, id):
    instance = get_object_or_404(FoodCategory,id=id)
    if request.method == "POST":
        form = FoodCategoryForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:food_category'))
        else:
            pass
    else:
        form = FoodCategoryForm(instance=instance)
        context={
            "title" : "food_category | Dashboard",
            "sub_title" : "food_categorys",
            "name" : "food_category",
            "form" : form,

        }
        return render(request, 'manager/update_food_category.html', context=context) 
                    
def food_category_delete(request, id):
    instance = get_object_or_404(FoodCategory,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:food_category'))