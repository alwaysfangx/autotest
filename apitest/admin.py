from django.contrib import admin
from apitest.models import Apitest,Apistep,Apis
# Register your models here.

class ApistepAdmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','creat_time','id','apitest']
    model = Apistep
    extra = 1

class ApitestAdmin(admin.ModelAdmin):
    list_display = ['apitestname','apitester','apitestresult','create_time','id']
    inlines = [ApistepAdmin]

class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'creat_time', 'id','product']
    model = Apis
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','create_time','id']
    inlines = [ApisAdmin]

admin.site.register(Apitest,ApitestAdmin)
# admin.site.register(Apistep,ApistepAdmin)
# admin.site.register(Apistep)
admin.site.register(Apis)