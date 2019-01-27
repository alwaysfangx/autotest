from django.contrib.auth.models import User
from django.shortcuts import render
from set.models import Set
# Create your views here.

def set_manage(request):
    username = request.session.get('user','')
    set_list = Set.objects.all()
    return render(request,"set_manage.html",{"user":username,"sets":set_list})


def set_user(request):
    user_list = User.objects.all()
    username = request.session.get('user','')
    return render(request,"set_manage.html",{"user":username,"users":user_list})

