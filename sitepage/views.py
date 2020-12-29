from django.shortcuts import render,redirect
from django.db.models import Q
from .models import lists
from .forms import getform
import time
import discord
# Create your views here.
def toppage(request): 
    return render(request,"toppage.html")
def search(request,name):
    if name:
       posts = lists.objects.all().order_by('Name')
       posts = posts.filter(
       Q(Name__icontains=name)).distinct()
    else:
       posts = Post.objects.all().order_by('Name')
    if posts.count==int("0"):
        html=""
    else:
        values=posts
        html=values
    a=posts.values
    
    date={"name":name,"posts":posts,"html":html,"a":a
         }
    return render(request,"search.html",date)
def date(request,date):
    form = getform()
    if request.method == 'POST':
       form = getform(request.POST)
       if form.is_valid():
        form.save(commit=True)
        return redirect("getok")
       else:
        listdate = lists.objects.get(pk=date)
        henkann={"name":listdate.Name,"money":listdate.money,"error":"すべて入力してください","form":form}
        return render(request,"date.html")
    else:
       listdate = lists.objects.get(pk=date)
       henkann={"name":listdate.Name,"money":listdate.money,"error":"","form":form,"pkid":str(date)}
       return render(request,"date.html",henkann)
def getok(request):
    return render(request,"getok.html")
