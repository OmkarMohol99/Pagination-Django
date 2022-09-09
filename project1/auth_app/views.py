from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def signupView(request):
    form = UserCreationForm()
    template_name = 'auth/signup.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin_url")
    context = {'form':form}
    return render(request, template_name, context)

def signinView(request):
    template_name = 'auth/signin.html'
    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')

        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect("show_url")
        messages.error(request, ' INVALID')

    context = {}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('signin_url')