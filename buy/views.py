from django.shortcuts import render
from .models import Policy

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def buy_side(request):
    return render(request, 'buy_side.html')

def buy_prof(request):
    return render(request,'buy_prof.html')

def prod_page(request):
    pol = Policy.objects.all()
    return render(request,'prod_page.html',{'pol':pol})

def prod_detail(request):
    return render(request,'prod_detail.html')
