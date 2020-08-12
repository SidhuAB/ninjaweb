from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def buy_side(request):
    return render(request, 'buy_side.html')
