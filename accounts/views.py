from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def signup(request):
    return render(request, 'signup.html')
