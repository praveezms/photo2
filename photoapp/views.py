from django.shortcuts import render
from django.http import HttpResponse
from photoapp.models import *
# Create your views here.
def home(request):
    return render(request,"gallery.html",{})
