from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, offer

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request,'index.html', {'products': products})


    #return HttpResponse('Hello Chandra')


def new(request):
    return HttpResponse('Hello new')

