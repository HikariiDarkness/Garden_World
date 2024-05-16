from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .forms import UserRegisterForm, formCrop

# Create your views here.

def index(request):
    #Home page for Garden World
    return render(request, 'Garden_World/index.html')

@login_required
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

def new_crop(request):
    if request.method == 'POST':
        form = formCrop(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            title = form.cleaned_data['title']
            messages.success(request, f'El cultivo: {title} ha sido creado')
            return redirect('Garden_World:homesite')
    else:
        form = formCrop()
    return render(request, 'Garden_World/new_crop.html', {
        'form': form
    })