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