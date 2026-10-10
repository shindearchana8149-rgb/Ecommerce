from django.shortcuts import render,get_object_or_404
from .models import Product
def home(request): return render(request,"store/home.html",{"products":Product.objects.all()})
def product(request,id): return render(request,"store/product.html",{"p":get_object_or_404(Product,id=id)})
