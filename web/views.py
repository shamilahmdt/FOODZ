from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from users.models import User
from customer.models import Customer,Cart,Address,CartBill,Order,OrderItem,Offer
from restaurant.models import StoreCategory, Store, Slider,FoodCategory,FoodItem
from django.db.models import Sum,Count




@login_required(login_url='/login')
def index(request):
    store_categories = StoreCategory.objects.all()
    stores = Store.objects.all()
    sliders = Slider.objects.all()

    context = {
        "store_categories" : store_categories,
        "stores" : stores,
        "sliders" : sliders,
    }
    return render(request, 'web/index.html', context=context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('web:index'))

        else:
            context = {
                "error" : True,
                "message": "Invalid Email or Password"
            }
            return render(request, 'web/login.html', context=context)
    else:         
        return render(request, 'web/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            context = {
                "error" : True,
                "message": "Email already exists"
            }
            return render(request, 'web/register.html', context=context)

        else:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                is_customer=True
            )
            user.save()

            customer = Customer.objects.create(
                user=user
            )
            customer.save()
            return HttpResponseRedirect(reverse('web:login'))

    else:
        return render(request, 'web/register.html')
    
def restaurants(request, id):
    store_categories = StoreCategory.objects.all()
    stores = Store.objects.all()

    selected_category = StoreCategory.objects.get(id=id)
    store = stores.filter(category=selected_category)

    context = {
        "store_categories" : store_categories,
        "store" : store,
        }
    return render(request, 'web/restaurant.html', context=context)

def single_rest(request, id):
    store = Store.objects.get(id=id)
    food_category =FoodCategory.objects.filter(restaurant=store)
    products = FoodItem.objects.filter(restaurant=store)
    carts = Cart.objects.all()

    products_with_quantities = []
    for product in products:
        cart_item = carts.filter(product=product).first()

        if cart_item:
            quantity = cart_item.qty
        else:
            quantity = 0

        products_with_quantities.append({
            'product' : product,
            'quantity' : quantity,
            "cart" : cart_item
        })

    items = 0
    amount = 0

    
    for cart in carts:
        items += 1
        amount += cart.amnt


    context = {
        "store" : store,
        "food_category" : food_category,
        "items" : items,
        "amount" : amount,
        "products_with_quantities" : products_with_quantities,
        "carts":carts,
        }

    return render(request, 'web/single_rest.html', context=context)

def single_rest_plus(request, id):
    cart = Cart.objects.get(id=id)
    price = cart.product.price
    store = cart.store

    cart.qty += 1
    cart.amnt += price
    cart.save()

    return HttpResponseRedirect(reverse('web:single_rest',kwargs={"id":store.id}))



def single_rest_minus(request, id):
    cart = Cart.objects.get(id=id)
    price = cart.product.price
    store = cart.store

    if cart.qty > 0:
        cart.qty -= 1
        cart.amnt -= price
        cart.save()
    else:
        cart.delete()



    return HttpResponseRedirect(reverse('web:single_rest',kwargs={"id":store.id}))




def cart(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    carts = Cart.objects.filter(customer=customer)
    addresses = Address.objects.filter(customer=customer)

    if CartBill.objects.filter(customer=customer).exists():
        cart_bill = CartBill.objects.get(customer=customer)
    else:
        cart_bill = CartBill.objects.create(
            customer = customer,
        )
        cart_bill.save()

    selected_address= None
    for address in addresses:
        if address.is_selected:
            selected_address = address

    store = None  
    for cart in carts:
        store = cart.store
        if cart.qty == 0:
            cart.delete()
            return HttpResponseRedirect(reverse('web:cart'))

        
    sub_total =  carts.aggregate(Sum('amnt'))['amnt__sum'] or 0    
    total = sub_total - cart_bill.offer_amnt

    context = {
        "store" : store,
        "carts" : carts,
        "selected_address" : selected_address,
        "sub_total" : sub_total,
        "total" : total,
        "cart_bill" : cart_bill,
        
        }

    return render(request, 'web/cart.html',context=context)

@login_required(login_url='/login')
def cart_add(request, id):
    user = request.user
    customer = Customer.objects.get(user=user)
    product = FoodItem.objects.get(id=id)
    store = product.restaurant
    price = product.price

    carts = Cart.objects.filter(customer=customer)

    for cart in carts:

        cart_store = cart.store
        if not cart_store == store:
            cart.delete()
        
    
    cart = Cart.objects.create(
        customer = customer,
        product = product,
        qty = 1,
        store = store,
        amnt = price
    )

    cart.save()

    return HttpResponseRedirect(reverse('web:single_rest',kwargs={"id":store.id}))


def cart_plus(request, id):
    cart = Cart.objects.get(id=id)
    price = cart.product.price

    cart.qty += 1
    cart.amnt += price
    cart.save()

    return HttpResponseRedirect(reverse('web:cart'))


def cart_minus(request, id):
    cart = Cart.objects.get(id=id)
    price = cart.product.price

    if cart.qty > 0:
        cart.qty -= 1
        cart.amnt -= price
        cart.save()

    else:
        cart.delete()



    return HttpResponseRedirect(reverse('web:cart'))


def address(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    addresses = Address.objects.filter(customer=customer)

    context = {
        "addresses" : addresses,
    }
    return render(request, 'web/address.html',context=context)

def add_address(request):
    user = request.user
    customer = Customer.objects.get(user=user)

    if request.method == 'POST':
        address = request.POST.get('address')
        appartment = request.POST.get('appartment')
        landmark = request.POST.get('landmark')
        address_type = request.POST.get('address_type')

        customer_address = Address.objects.create(
            customer = customer,
            address = address,
            appartment = appartment,
            landmark = landmark,
            address_type = address_type,
        )
        customer_address.save()

        return HttpResponseRedirect(reverse('web:address'))

    else:

        return render(request, 'web/add_address.html')

def edit_address(request, id):
    addr = Address.objects.get(id=id)

    if request.method == 'POST':
        address = request.POST.get('address')
        appartment = request.POST.get('appartment')
        landmark = request.POST.get('landmark')
        address_type = request.POST.get('address_type')


        addr.address = address,
        addr.appartment = appartment,
        addr.landmark = landmark,
        addr.address_type = address_type,
        
        addr.save()

        return HttpResponseRedirect(reverse('web:address'))

    else:
        context = {
            "address" : addr,
        }
        return render(request, 'web/add_address.html',context=context)

def delete_address(request, id):
    address = Address.objects.get(id=id)
    address.delete()

    return HttpResponseRedirect(reverse('web:address'))
    
def select_address(request, id):
    selected_address = Address.objects.get(id=id)
    addresses = Address.objects.all()
    
    for address in addresses:
        if address == selected_address:
            address.is_selected=True
            address.save()
        else:
            address.is_selected=False
            address.save()
                

    return HttpResponseRedirect(reverse('web:address'))

def checkout(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    carts = Cart.objects.filter(customer=customer)
    cart_bill = CartBill.objects.get(customer=customer)
    sub_total =  carts.aggregate(Sum('amnt'))['amnt__sum']       
    total = sub_total - cart_bill.offer_amnt
    
    context = {
        "cart_bill": cart_bill,
        "sub_total" : sub_total,
        "total" : total,

        }

    return render(request, 'web/checkout.html',context=context)

def account(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    orders = Order.objects.filter(customer=customer)
    order_items = OrderItem.objects.filter(customer=customer)

    order_item_count = []
    for order in orders:
        count = 0 
        for order_item in order_items:
            if order_item.order == order:
                count +=1

        order_item_count.append({
            "order" : order,
            "count" : count,

        })

    context = {
        "orders" : orders,
        "customer" : customer,
        "order_item_count" : order_item_count,
        }

    return render(request, 'web/account.html',context=context)

def place_order(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    addresses = Address.objects.filter(customer=customer)
    cart_bill = CartBill.objects.get(customer=customer)


    for addr in addresses:
        if addr.is_selected:
            address = addr

    carts = Cart.objects.filter(customer=customer)
    for cart in carts:
        store = cart.store

    sub_total = carts.aggregate(Sum('amnt'))['amnt__sum'] or 0
    total = sub_total - cart_bill.offer_amnt


    previous = Order.objects.all().first()

    if previous:
        order_id = f'ORD00{previous.id+1}'
    else:
        order_id = 'ORD001'

    order = Order.objects.create(
        order_id = order_id,
        customer = customer,
        address = address,
        sub_total = sub_total,
        status = 'PL',
        total = total,
        store = store,
    )    

    for cart in carts:
        order_item = OrderItem.objects.create(
            customer = customer,
            order = order,
            product = cart.product,
            qty = cart.qty,
            store = cart.store,
            amnt = cart.amnt
        )            
        cart.delete()

    cart_bill.coupen_code = None
    cart_bill.offer_amnt = 0
    cart_bill.save()

    return HttpResponseRedirect(reverse('web:account'))


def offer(request):
    offers = Offer.objects.all()

    context = {
        "offers" : offers,
        }

    
    return render(request, 'web/offer.html',context=context)

def offer_apply(request,id):
    user = request.user
    customer = Customer.objects.get(user=user)
    offer = Offer.objects.get(id=id)
    total = Cart.objects.filter(customer=customer).aggregate(Sum('amnt'))['amnt__sum']

    if offer.is_percentage:
        offer_amnt = total*(offer.offer/100)
    else:
        offer_amnt = offer.offer

    cart_bill = CartBill.objects.get(customer=customer)
    cart_bill.offer_amnt = offer_amnt
    cart_bill.coupen_code = offer.coupen_code
    cart_bill.save()

    return HttpResponseRedirect(reverse('web:cart'))


    

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('web:login'))

