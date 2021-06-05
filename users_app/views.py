from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

def index(request):
    context = {
        "some_data": Users.objects.all()
    }
    return render(request, "index.html", context)

def redirect_method(request):
    if request.method=='POST':
        Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email'], age=request.POST['age'])
    return redirect('/')
