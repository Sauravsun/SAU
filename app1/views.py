from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def blog(request):
    return render(request,'blog.html')

def shop(request):
    return render(request,'shop.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def wishlist(request):
    return render(request,'wishlist.html')


def product(request):
    return render(request,'product-details.html')

def baudio(request):
    return render(request,"blog-details-audio.html")  

def bgallery(request):
    return render(request,"blog-details-gallery.html")


def bimage(request):
    return render(request,"blog-details-image.html")


def bvideo(request):
    return render(request,"blog-details-video.html")


def bright(request):
    return render(request,"blog-details-right-sidebar.html")


def register(request):
    if request.method=='POST':
        mail=request.POST['regemail']
        password=request.POST['regpass']
        add=registertb(email=mail,passw=password)
        add.save()
        return render(request,"login.html")
    
    else:
         return render(request,"register.html")


def logint(request):
    if request.method=='POST':
        user=request.POST['username_email']
        passwo=request.POST['password']
        were=registertb.objects.filter(email=user)
        if were:
            for i in were:
                pas=i.passw
                if pas==passwo:
                    for x in were:
                        request.session['id']=x.id
                        request.session['email']=x.email
                    return render(request,"index.html")
                else:
                     return render(request,"login.html",{'mess':"not registerd pass"})
        else:
            return render(request,"login.html",{'mess':"not registerd email"})
    else:
            return render(request,"login.html",{'mess':"not registerd enter valid details"})     



#admin
def ind(request):
    # if request.session.has_key("aid"):
    return render(request,"admin1/index.html")
    # else:
    #     return render(request,"admin1/login.html")            


def base(request):
    
        return render(request,'admin1/basic_table.html')


def form(request):
    return render(request,"admin1/form_component.html")


def product(request):
    return render(request,'admin1/product_table.html')
 
   

    
