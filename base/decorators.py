

from django.http import HttpResponse
from django.shortcuts import redirect, resolve_url
import time

day = time.localtime()


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_fun(request, *args , **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request , *args , **kwargs)
            else:
                return HttpResponse("Hal kan Laguuma Ogola ")
        return wrapper_fun
    return decorator

def IsMatchDay(view):
    def wrapper_func(request , *args , **kwargs):
        if day.tm_wday != 3:
            return redirect('home')
        else:
            while day.tm_hour < 15:
                return view(request , *args , **kwargs)
            else:
                return HttpResponse("Fadlan wakhtigii la gudbinayay fasax waa la dhaafay wixii warbixin ah u reeb guddiga oo la hadal ")
    return  wrapper_func

def Line_up_avialable(view):
    def wrapper_func(request , *args , **kwargs):
        if day.tm_wday != 3:
            return redirect('home')
        else:
            while day.tm_hour < 15:
                return HttpResponse(" waiting for all player to make attendence !!!")
            else:
                return view(request , *args , **kwargs)
    return  wrapper_func