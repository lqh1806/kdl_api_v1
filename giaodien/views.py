from django.shortcuts import render
from sale.views import *
# Create your views here.

def sale(request):
    return render(request, 'sale.html')

def store(request):
    return render(request, 'store.html')    