import email
from http.client import HTTPResponse
import json
from math import ceil
from os import name
from turtle import update
from unicodedata import category
from urllib import response
import django
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contact, Product,Orders,OrderUpdate
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
   
    # params = {'no_of_Slides':noofSlides,'range':range(1,noofSlides),'product': products}
    # allprods = [[products,range(1,noofSlides),noofSlides],
    #             [products,range(1,noofSlides),noofSlides]]
    allprods = []
    catprods = Product.objects.values('Category','id')
    cats = {items['Category'] for items in catprods}
    for cat in cats:
        prod = Product.objects.filter(Category = cat)
        n = len(products)
        noofSlides = n//4 + ceil((n/4)+(n//4))
        allprods.append([prod,range(1,noofSlides),noofSlides])
    params = {'allprods':allprods}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method == 'POST':
        names = request.POST.get('name','')
        emails = request.POST.get('email','')
        phones = request.POST.get('phone','')
        descp = request.POST.get('desc','')
        print(names,emails,phones,descp)
        contact = Contact(name=names,email=emails,phone=phones,desc=descp)
        contact.save()
        thanks = True
        return render(request,'shop/contact.html',{'thanks':thanks})
    return render(request,'shop/contact.html')

def tracker(request):
    if request.method == 'POST':
        orderid = request.POST.get('orderid','')
        emails = request.POST.get('email','')
        try:
            order = Orders.objects.filter(order_id=orderid,email=emails)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response= json.dumps({'status':"success",'updates':updates,'itemjson':order[0].items_json},default=str)
                return HttpResponse(response)

            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
                return HttpResponse('{"status":"error"}')
    return render(request,'shop/tracker.html')


def searchMatch(query,item):
    price = str(item.price)
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.Category.lower() or query in item.subcategory.lower() or query in price.lower() :
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allprods = []
    catprods = Product.objects.values('Category','id')
    cats = {items['Category'] for items in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(Category = cat)
        prod = [item for item in prodtemp if searchMatch(query,item)]
        n = len(prod)
        noofSlides = n//4 + ceil((n/4)+(n//4))
        if len(prod) != 0:
            allprods.append([prod,range(1,noofSlides),noofSlides])
    params = {'allprods':allprods, 'msg':""}
    if(len(allprods) == 0 or len(query) < 4):
        params ={'msg':"The item you are Search is not Avialable Please try Searching with Different Names"}
    return render(request,'shop/search.html',params)

def product(request,myid):
    # fetch product using id 
    products = Product.objects.filter(id = myid)
    return render(request,'shop/product.html',{'product':products[0]})

def checkout(request):
    if request.method == 'POST':
        items_jsons = request.POST.get('itemsJson','')
        c_names = request.POST.get('name','')
        c_amount = request.POST.get('amount','')
        c_emails = request.POST.get('email','')
        c_phone = request.POST.get('phone','')
        c_address = request.POST.get('address1','') + "  " + request.POST.get('address2','')
        c_city = request.POST.get('city','')
        c_state = request.POST.get('state','')
        c_pincode = request.POST.get('pincode','')
        order = Orders(items_json=items_jsons,amount=c_amount,name=c_names,email=c_emails,phone=c_phone,address=c_address,city=c_city,state=c_state,pincode=c_pincode)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="the order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
    return render(request,'shop/checkout.html')