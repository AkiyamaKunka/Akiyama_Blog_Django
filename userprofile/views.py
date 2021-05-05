from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .form import UserLoginForm, UserRegisterForm, ProfileForm
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
        return HttpResponse("Submit your data with either POST or GET")

def user_logout(request):
    logout(request)
    return redirect('index_page')

def user_register(request):
    if request.method == 'POST':
        new_register_form = UserRegisterForm(data = request.POST)
        if new_register_form.is_valid():
            new_register_user = new_register_form.save(commit = False)
            new_register_user.set_password(new_register_form.cleaned_data['password'])
            new_register_user.save()
            login(request, new_register_user)
            return redirect('article:article_list')
        else:
            return HttpResponse("Error Form")
    elif request.method == 'GET':
        empty_user_register_form = UserRegisterForm()
        context = {'emtpy_user_register_form' : empty_user_register_form}
        return render(request, 'register.html', context)
    else:
        return HttpResponse("Submit your data with either POST or GET")

@login_required(login_url='/user_profile/login/')
# @login_required is a python decorator,
# if user is not logged in when the function is called, it will redirect to this url
def user_delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id = id)
        if request.user == user:
            logout(request)
            user.delete()
            return redirect('index_page')
        else:
            return HttpResponse("You do not have the right to delete")
    else:
        return HttpResponse("Only accept post request")

@login_required(login_url='/user_profile/login/')
def profile_edit(request, id):
    user = User.objects.get(id = id)
    profile = Profile.objects.get(user_id = id)
    if request.method == "POST":
        if request.user.id == user.id:
            new_form = ProfileForm(data=request.POST)
            if new_form.is_valid():
                profile_data_cd = new_form.cleaned_data
             #  profile.avatar = profile_data_cd['avatar']
                profile.phone = profile_data_cd['phone']
                profile.bio = profile_data_cd['bio']
                profile.save()
                return redirect('user_profile:profile_edit', id=id)
            else:
                return HttpResponse("Data of form is invalid")
        else:
            return HttpResponse("You do not have right to change user's profile")
    elif request.method == "GET":
        empty_profile_form = ProfileForm()
        context = {'empty_profile_form' : empty_profile_form, 'profile' : profile, 'user' : user}
        return render(request, 'profile_edit.html', context)
    else:
        return HttpResponse("Please request in method either POST or GET")