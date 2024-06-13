from django.shortcuts import render,redirect
from django.views.generic import ListView,View,CreateView
from store.models import Categorymod,Productmod,cartmod,ordermod
from django.contrib.auth.models import User
from store.form import regform,loginform,orderform
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
# Create your views here.

#decoroter
def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


class homeview(ListView):
    model=Categorymod
    template_name="store\index.html"
    context_object_name="categories"
    
class category_data(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Productmod.objects.filter(category_id=id)
        name=Categorymod.objects.get(id=id)
        return render(request,"store/cat_data.html",{"data":data,"name":name})
    

class product_data(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Productmod.objects.get(id=id)
        return render(request,"store/pro_data.html",{"data":data})
    

class regview(CreateView):
    template_name="store/reg.html"
    form_class=regform
    model=User
    success_url=reverse_lazy("login")

class loginview(View):
    def get(self,request,*args,**kwargs):
        form=loginform()
        return render(request,"store/login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=loginform(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_obj=authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                return redirect("home")
        return redirect("home")
    
class logoutview(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("home")
    
#call decorator
@method_decorator(signin_required,name="dispatch")
class cartview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Productmod.objects.get(id=id)
        cartmod.objects.create(item=data,user=request.user)
        print("added successfully")
        return redirect("home")


class cart_deleteview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cartmod.objects.get(id=id).delete()
        return redirect("home")
    
@method_decorator(signin_required,name="dispatch")
class cart_dataview(View):
    def get(self,request,*args,**kwargs):
        data=cartmod.objects.filter(user=request.user)
        return render(request,"store/cart_data.html",{"data":data})

@method_decorator(signin_required,name="dispatch")
class orderview(View):
    def get(self,request,*args,**kwargs):
        form=orderform()
        return render(request,"store/order.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        data=Productmod.objects.get(id=id)
        form=orderform(request.POST)
        if form.is_valid():
            qs=form.cleaned_data.get("address")
            ordermod.objects.create(address=qs,order_item=data,customer=request.user)
            return redirect("home")
        return redirect("cart")
    
@method_decorator(signin_required,name="dispatch")
class orderlist(View):
    def get(self,request,*args,**kwargs):
        data=ordermod.objects.filter(customer=request.user)
        return render(request,"store/orderlist.html",{"data":data})

@method_decorator(signin_required,name="dispatch")
class orderdelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get(id=id)
        data=ordermod.objects.delete()
        return redirect("ordlist")
    
class searchview(View):
    def get(self,request,*args,**kwargs):
        query=request.GET.get("q")
        if query:
            result=Productmod.objects.filter(name__icontain=query)
        else:
            result=None
        return render(request,"store/search.html",{"result":result})
