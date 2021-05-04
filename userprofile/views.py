from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .form import UserLoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def user_login(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data = request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username = data['username'], password = data['password'])
            if user:
                login(request, user)
                return redirect("index_page")
            else:
                return HttpResponse("Wrong Username or Password")
        else:
            return HttpResponse("Error Form")
    elif request.method == "GET":
        empty_login_form = UserLoginForm()
        context = {'empty_login_form' : empty_login_form}
        return render(request, 'user_login.html', context)
    else:
        return HttpResponse("Upload your data with either POST or GET")

def user_logout(request):
    logout(request)
    return redirect('index_page')