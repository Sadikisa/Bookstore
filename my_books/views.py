from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def sadik(request):
  
   return render(request,'jiyali.html')


def shop(request):
  
   return render(request,'shop.html')
def category(request):
  
   return render(request,'categories.html')
def about(request):
    return render(request,'about.html')