from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignInForm, SignUpForm
from django.contrib.auth.models import User
from authentication.models import Profile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse





def index(request):
    return HttpResponse('It works!!!')


def sign_in(request):
    form = SignInForm()

    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")

    return render(request, 'authentication/sign_in.html', locals())



def sign_up(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User()
            user.username = form.cleaned_data.get("username")
            user.email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user.set_password(password)
            user.save()
            Profile.objects.create(user=user)

            return redirect('/')

    return render(request, 'authentication/sign_up.html', locals())


def sign_out(request):
    logout(request)
    return redirect("/")





