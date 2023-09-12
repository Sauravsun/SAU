from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path("",views.index),
    path("about/",views.about),
    path('contact/',views.contact),
    path('blog/',views.blog),
    path('shop/',views.shop),
    path('cart/',views.cart),
    path('checkout/',views.checkout),
    path('wish/',views.wishlist),
    path('product/',views.product),
    path('baudio/',views.baudio),
    path('bgallery/',views.bgallery),
    path('bimage/',views.bimage),
    path('bvideo/',views.bvideo),
    path('bsidebar/',views.bright),
    path('login/',views.logint),
    path('register/',views.register),
    #admin
    path('admin-index/',views.ind),
    path("base/",views.base),
    path("form/",views.form),
    path("product/",views.product),
]
