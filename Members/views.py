
from django.shortcuts import render, redirect
from .models import User

from django.contrib import messages
from django.http.response import HttpResponse

from .forms import userForm, CreateUserForm, createProfileUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User Doesn't exit .......")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "user or password is not correct...")
            return redirect('login')

    context = {'page': page}
    return render(request, 'members/login_register.html', context)


def logoutpage(requset):
    logout(requset)
    return redirect('home')


def registerpage(request):
    page = 'register'

    form = CreateUserForm()
    profile_form = createProfileUser()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile_form = createProfileUser(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "error occoured during registration")
    context = {'page': page, 'form': form, 'profile': profile_form}
    return render(request, 'members/login_register.html', context)


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    profile = createProfileUser(instance=request.user.profileuser)
    form = userForm(instance=user)
    if request.method == 'POST':
        form = userForm(request.POST, instance=user)
        profile = createProfileUser(request.POST, request.FILES ,instance=request.user.profileuser)
        if form.is_valid() and profile.is_valid():
            user = form.save()
            profile = profile.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('home')
    context = {'form': form , 'profile':profile}
    return render(request, 'members/update-user.html', context)



