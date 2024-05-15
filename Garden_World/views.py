from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.

def index(request):
    #Home page for Garden World
    return render(request, 'Garden_World/index.html')

def homesite(request):
    return render(request, 'Garden_World/homesite.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} ha sido creado')
            return redirect('Garden_World:homesite')
    else:
        form= UserRegisterForm()
    context = {'form' : form}
    return render(request, 'Garden_World/register.html', context)

