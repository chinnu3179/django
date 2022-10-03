from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
    # return HttpResponse("<h1>Hii Django HOME</h1>")
    return render(request,'home.html',{})

def contact_view(request,*args,**kwargs):
    return render(request,'contact.html',{})
    # return HttpResponse("<h1>Hii Django CONTACT</h1>")

def about_view(request,*args,**kwargs):
    return render(request,'about.html',{})
    # return HttpResponse("<h1>Hii Django about</h1>")

def social_view(request,*args,**kwargs):
    return render(request,'social.html',{})
    # return HttpResponse("<h1>Hii Django social</h1>")