from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from webtest.models import Webcasestep,Webcase
# Create your views here.

@login_required
def webcase_manage(request):
    webcase_list = Webcase.objects.all()
    username = request.session.get('user','')
    return render(request,"webcase_manage.html",{"user":username,"webcases":webcase_list})

@login_required
def webcasesteo_manage(requset):
    username = requset.session.get('user','')
    webcasestep_list = Webcasestep.objects.all()
    return render(requset,"webcasestep_manage.html",{"user":username,"webcasesteps":webcasestep_list})