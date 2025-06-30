from django.shortcuts import get_object_or_404, render,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from users.models import User
from customer.models import *
from restaurant.models import *

from .form import *
from common.functions import *


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
            message = generate_form_errors(form)
            form = StoreCategoryForm()
            context={
            "title" : "Store Categories | Dashboard",
            "sub_title" : "Store Categories",
            "name" : "Create Store Categories",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/update_store_category.html', context=context)
            
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
            message = generate_form_errors(form)
            form = StoreCategoryForm()
            context={
            "title" : "Store Categories | Dashboard",
            "sub_title" : "Store Categories",
            "name" : "Create Store Categories",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/update_store_category.html', context=context)
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

def orders(request):
    instances = Order.objects.all()
    context={
        "instances" : instances,
    }
    return render(request, 'manager/order.html', context=context) 

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
            message = generate_form_errors(form)
            form = StoreForm()
            context={
            "title" : "Store | Dashboard",
            "sub_title" : "Stores",
            "name" : "Store",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/update_store.html', context=context)
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
            message = generate_form_errors(form)
            form = StoreForm()
            context={
            "title" : "Store | Dashboard",
            "sub_title" : "Stores",
            "name" : "Store",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/update_store.html', context=context)
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
            message = generate_form_errors(form)
            form = SliderForm()
            context={
            "title" : "slider | Dashboard",
            "sub_title" : "sliders",
            "name" : "slider",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/update_slider.html', context=context)
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
            message = generate_form_errors(form)
            form = SliderForm()
            context={
            "title" : "slider | Dashboard",
            "sub_title" : "sliders",
            "name" : "slider",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/update_slider.html', context=context)
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

def food_item(request):
    instances = FoodItem.objects.all()

    context={
        "title" : "food_item | Dashboard",
        "sub_title" : "food_items",
        "name" : "food_item",
        "instances" : instances,

    }
    return render(request, 'manager/food_item.html', context=context)

def food_item_create(request):
    if request.method == "POST":
        form = FoodItemForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:food_item'))
        
        else:
            message = generate_form_errors(form)
            form = FoodItemForm()
            context={
            "title" : "food_item | Dashboard",
            "sub_title" : "food_items",
            "name" : "food_item",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/update_food_item.html', context=context)
    else:
        form = FoodItemForm()
        context={
            "title" : "food_item | Dashboard",
            "sub_title" : "food_items",
            "name" : "food_item",
            "form" : form,

        }
        return render(request, 'manager/update_food_item.html', context=context)

def food_item_update(request, id):
    instance = get_object_or_404(FoodItem,id=id)
    if request.method == "POST":
        form = FoodItemForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:food_item'))
        else:
            message = generate_form_errors(form)
            form = FoodItemForm()
            context={
            "title" : "food_item | Dashboard",
            "sub_title" : "food_items",
            "name" : "food_item",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/update_food_item.html', context=context)
    else:
        form = FoodItemForm(instance=instance)
        context={
            "title" : "food_item | Dashboard",
            "sub_title" : "food_items",
            "name" : "food_item",
            "form" : form,

        }
        return render(request, 'manager/update_food_item.html', context=context) 
                    
def food_item_delete(request, id):
    instance = get_object_or_404(FoodItem,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:food_item'))

def food_category(request):
    instances = FoodCategory.objects.all()

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
            message = generate_form_errors(form)
            form = FoodCategoryForm()
            context={
            "title" : "food_category | Dashboard",
            "sub_title" : "food_categorys",
            "name" : "food_category",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/update_food_category.html', context=context)
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
            message = generate_form_errors(form)
            form = FoodCategoryForm()
            context={
            "title" : "food_category | Dashboard",
            "sub_title" : "food_categorys",
            "name" : "food_category",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/update_food_category.html', context=context)
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

def customer(request):
    instances = Customer.objects.all()

    context={
        "title" : "customer | Dashboard",
        "sub_title" : "customers",
        "name" : "customer",
        "instances" : instances,

    }
    return render(request, 'manager/customer.html', context=context)

def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:customer'))
        
        else:
            message = generate_form_errors(form)
            form = CustomerForm()
            context={
            "title" : "customer | Dashboard",
            "sub_title" : "customers",
            "name" : "customer",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/customer_update.html', context=context)
    else:
        form = CustomerForm()
        context={
            "title" : "customer | Dashboard",
            "sub_title" : "customers",
            "name" : "customer",
            "form" : form,

        }
        return render(request, 'manager/customer_update.html', context=context)

def customer_update(request, id):
    instance = get_object_or_404(Customer,id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:customer'))
        else:
            message = generate_form_errors(form)
            form = CustomerForm()
            context={
            "title" : "customer | Dashboard",
            "sub_title" : "customers",
            "name" : "customer",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/customer_update.html', context=context)
    else:
        form = CustomerForm(instance=instance)
        context={
            "title" : "customer | Dashboard",
            "sub_title" : "customers",
            "name" : "customer",
            "form" : form,

        }
        return render(request, 'manager/customer_update.html', context=context) 
                    
def customer_delete(request, id):
    instance = get_object_or_404(Customer,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:customer'))

def address(request):
    instances = Address.objects.all()

    context={
        "title" : "address | Dashboard",
        "sub_title" : "addresss",
        "name" : "address",
        "instances" : instances,

    }
    return render(request, 'manager/address.html', context=context)



def address_create(request):
    if request.method == "POST":
        form = AddressForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:address'))
        
        else:
            message = generate_form_errors(form)
            form = AddressForm()
            context={
            "title" : "address | Dashboard",
            "sub_title" : "addresss",
            "name" : "address",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/address_update.html', context=context)
    else:
        form = AddressForm()
        context={
            "title" : "address | Dashboard",
            "sub_title" : "addresss",
            "name" : "address",
            "form" : form,

        }
        return render(request, 'manager/address_update.html', context=context)

def address_update(request, id):
    instance = get_object_or_404(Address,id=id)
    if request.method == "POST":
        form = AddressForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:address'))
        else:
            message = generate_form_errors(form)
            form = AddressForm()
            context={
            "title" : "address | Dashboard",
            "sub_title" : "addresss",
            "name" : "address",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/address_update.html', context=context)
    else:
        form = AddressForm(instance=instance)
        context={
            "title" : "address | Dashboard",
            "sub_title" : "addresss",
            "name" : "address",
            "form" : form,

        }
        return render(request, 'manager/address_update.html', context=context) 
                    
def address_delete(request, id):
    instance = get_object_or_404(Address,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:address'))

def cart(request):
    instances = Cart.objects.all()

    context={
        "title" : "cart | Dashboard",
        "sub_title" : "carts",
        "name" : "cart",
        "instances" : instances,

    }
    return render(request, 'manager/cart.html', context=context)

def cart_create(request):
    if request.method == "POST":
        form = CartForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:cart'))
        
        else:
            message = generate_form_errors(form)
            form = CartForm()
            context={
            "title" : "cart | Dashboard",
            "sub_title" : "carts",
            "name" : "cart",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/cart_update.html', context=context)
    else:
        form = CartForm()
        context={
            "title" : "cart | Dashboard",
            "sub_title" : "carts",
            "name" : "cart",
            "form" : form,

        }
        return render(request, 'manager/cart_update.html', context=context)

def cart_update(request, id):
    instance = get_object_or_404(Cart,id=id)
    if request.method == "POST":
        form = CartForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:cart'))
        else:
            message = generate_form_errors(form)
            form = CartForm()
            context={
            "title" : "cart | Dashboard",
            "sub_title" : "carts",
            "name" : "cart",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/cart_update.html', context=context)
    else:
        form = CartForm(instance=instance)
        context={
            "title" : "cart | Dashboard",
            "sub_title" : "carts",
            "name" : "cart",
            "form" : form,

        }
        return render(request, 'manager/cart_update.html', context=context) 
                    
def cart_delete(request, id):
    instance = get_object_or_404(Cart,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:cart'))

def cartbill(request):
    instances = CartBill.objects.all()

    context={
        "title" : "cartbill | Dashboard",
        "sub_title" : "cartbills",
        "name" : "cartbill",
        "instances" : instances,

    }
    return render(request, 'manager/cartbill.html', context=context)

def cartbill_create(request):
    if request.method == "POST":
        form = CartBillForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:cartbill'))
        
        else:
            message = generate_form_errors(form)
            form = CartBillForm()
            context={
            "title" : "cartbill | Dashboard",
            "sub_title" : "cartbills",
            "name" : "cartbill",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/cartbill_update.html', context=context)
    else:
        form = CartBillForm()
        context={
            "title" : "cartbill | Dashboard",
            "sub_title" : "cartbills",
            "name" : "cartbill",
            "form" : form,

        }
        return render(request, 'manager/cartbill_update.html', context=context)

def cartbill_update(request, id):
    instance = get_object_or_404(CartBill,id=id)
    if request.method == "POST":
        form = CartBillForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:cartbill'))
        else:
            message = generate_form_errors(form)
            form = CartBillForm()
            context={
            "title" : "cartbill | Dashboard",
            "sub_title" : "cartbills",
            "name" : "cartbill",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/cartbill_update.html', context=context)
    else:
        form = CartBillForm(instance=instance)
        context={
            "title" : "cartbill | Dashboard",
            "sub_title" : "cartbills",
            "name" : "cartbill",
            "form" : form,

        }
        return render(request, 'manager/cartbill_update.html', context=context) 
                    
def cartbill_delete(request, id):
    instance = get_object_or_404(CartBill,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:cartbill'))

def full_orders(request):
    instances = Order.objects.all()

    context={
        "title" : "full_orders | Dashboard",
        "sub_title" : "full_orderss",
        "name" : "full_orders",
        "instances" : instances,

    }
    return render(request, 'manager/order.html', context=context)

def full_orders_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:orders'))
        
        else:
            message = generate_form_errors(form)
            form = OrderForm()
            context={
            "title" : "full_orders | Dashboard",
            "sub_title" : "full_orderss",
            "name" : "full_orders",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/order_update.html', context=context)
    else:
        form = OrderForm()
        context={
            "title" : "full_orders | Dashboard",
            "sub_title" : "full_orderss",
            "name" : "full_orders",
            "form" : form,

        }
        return render(request, 'manager/order_update.html', context=context)

def full_orders_update(request, id):
    instance = get_object_or_404(Order,id=id)
    if request.method == "POST":
        form = OrderForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:orders'))
        else:
            message = generate_form_errors(form)
            form = OrderForm()
            context={
            "title" : "full_orders | Dashboard",
            "sub_title" : "full_orderss",
            "name" : "full_orders",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/order_update.html', context=context)
    else:
        form = OrderForm(instance=instance)
        context={
            "title" : "full_orders | Dashboard",
            "sub_title" : "full_orderss",
            "name" : "full_orders",
            "form" : form,

        }
        return render(request, 'manager/order_update.html', context=context) 
                    
def full_orders_delete(request, id):
    instance = get_object_or_404(Order,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:orders'))

def order_item(request):
    instances = OrderItem.objects.all()

    context={
        "title" : "order_item | Dashboard",
        "sub_title" : "order_items",
        "name" : "order_item",
        "instances" : instances,

    }
    return render(request, 'manager/order_item.html', context=context)

def order_item_create(request):
    if request.method == "POST":
        form = OrderItemForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:order_item'))
        
        else:
            message = generate_form_errors(form)
            form = OrderItemForm()
            context={
            "title" : "order_item | Dashboard",
            "sub_title" : "order_items",
            "name" : "order_item",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/order_item_update.html', context=context)
    else:
        form = OrderItemForm()
        context={
            "title" : "order_item | Dashboard",
            "sub_title" : "order_items",
            "name" : "order_item",
            "form" : form,

        }
        return render(request, 'manager/order_item_update.html', context=context)

def order_item_update(request, id):
    instance = get_object_or_404(OrderItem,id=id)
    if request.method == "POST":
        form = OrderItemForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:order_item'))
        else:
            message = generate_form_errors(form)
            form = OrderItemForm()
            context={
            "title" : "order_item | Dashboard",
            "sub_title" : "order_items",
            "name" : "order_item",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/order_item_update.html', context=context)
    else:
        form = OrderItemForm(instance=instance)
        context={
            "title" : "order_item | Dashboard",
            "sub_title" : "order_items",
            "name" : "order_item",
            "form" : form,

        }
        return render(request, 'manager/order_item_update.html', context=context) 
                    
def order_item_delete(request, id):
    instance = get_object_or_404(OrderItem,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:order_item'))

def offer(request):
    instances = Offer.objects.all()

    context={
        "title" : "offer | Dashboard",
        "sub_title" : "offers",
        "name" : "offer",
        "instances" : instances,

    }
    return render(request, 'manager/order.html', context=context)

def offer_create(request):
    if request.method == "POST":
        form = OfferForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:orders'))
        
        else:
            message = generate_form_errors(form)
            form = OfferForm()
            context={
            "title" : "offer | Dashboard",
            "sub_title" : "offers",
            "name" : "offer",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/order_update.html', context=context)
    else:
        form = OfferForm()
        context={
            "title" : "offer | Dashboard",
            "sub_title" : "offers",
            "name" : "offer",
            "form" : form,

        }
        return render(request, 'manager/order_update.html', context=context)

def offer_update(request, id):
    instance = get_object_or_404(Offer,id=id)
    if request.method == "POST":
        form = OfferForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return HttpResponseRedirect(reverse('manager:orders'))
        else:
            message = generate_form_errors(form)
            form = OfferForm()
            context={
            "title" : "offer | Dashboard",
            "sub_title" : "offers",
            "name" : "offer",
            "error" : True,
            "message" :message,
            "form" : form,
            }
            return render(request, 'manager/order_update.html', context=context)
    else:
        form = OfferForm(instance=instance)
        context={
            "title" : "offer | Dashboard",
            "sub_title" : "offers",
            "name" : "offer",
            "form" : form,

        }
        return render(request, 'manager/order_update.html', context=context) 
                    
def offer_delete(request, id):
    instance = get_object_or_404(Offer,id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:orders'))