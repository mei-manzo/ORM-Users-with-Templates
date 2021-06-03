from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users
from .models import AddForm



def index(request):
    context = {
        "some_data": Users.objects.all()
    }
    return render(request, "index.html", context)

def redirect(request):
    this_form = AddForm(request.POST)
    if this_form.is_valid():
        first_name = this_form.cleaned_data['first_name']
        last_name = this_form.cleaned_data['last_name']
        email_address = this_form.cleaned_data['email']
        age = this_form.cleaned_data['age']
        new_user = Users(first_name=first_name, last_name=last_name, email=email_address, age=age)
    return render(request, "redirect.html", context)



# Create your views here.
