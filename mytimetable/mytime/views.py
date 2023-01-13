from django.shortcuts import render
from datetime import datetime
# Create your views here.

def home(request):
    return render(request,'myfirstapp/home.html',context)