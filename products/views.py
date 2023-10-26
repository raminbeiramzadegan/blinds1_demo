from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Products,Category
# Create your views here.





class ProductsList(View):
    def get(self,request):
        products = Products.objects.all()
        return render(request,'products/shop-grid-full.html',{'products':products})



class ProductDetailView(View):
    def get(self,request,slug):
        products = get_object_or_404(Products,slug=slug)
        return render(request,'products/product-detail.html',{'products':products})