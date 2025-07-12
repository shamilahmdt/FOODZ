import json

from django.http import HttpResponse
from django.shortcuts import reverse
from django.http import HttpResponseRedirect

def allow_super(function):
    def wrapper(request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_superuser:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                response_data = {
                    "status":"error",
                    "title":"Unathorized Access",
                    "message":"you can't perform this action"
                }
                return HttpResponse(json.dumps(response_data),content_type="applicatuins/json")
            else:
                return HttpResponseRedirect(reverse("manager:logout"))
            
        return function(request, *args, **kwargs)
    
    return wrapper

def allow_store(function):
    def wrapper(request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_store:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                response_data = {
                    "status":"error",
                    "title":"Unathorized Access",
                    "message":"you can't perform this action"
                }
                return HttpResponse(json.dumps(response_data),content_type="applicatuins/json")
            else:
                return HttpResponseRedirect(reverse("manager:logout"))
            
        return function(request, *args, **kwargs)
    
    return wrapper

def allow_agent(function):
    def wrapper(request, *args, **kwargs):
        current_user = request.user
        if not current_user.is_agent:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                response_data = {
                    "status":"error",
                    "title":"Unathorized Access",
                    "message":"you can't perform this action"
                }
                return HttpResponse(json.dumps(response_data),content_type="applicatuins/json")
            else:
                return HttpResponseRedirect(reverse("manager:logout"))
            
        return function(request, *args, **kwargs)
    
    return wrapper
