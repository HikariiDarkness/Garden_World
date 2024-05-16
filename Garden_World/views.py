from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, formCrop
from .models import Crop

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
            return redirect('Garden_World:login')
    else:
        form= UserRegisterForm()
    context = {'form' : form}
    return render(request, 'Garden_World/register.html', context)

@login_required
def new_crop(request):
    if request.method == 'POST':
        form = formCrop(request.POST, request.FILES)
        if form.is_valid():   
            form.save() 
            title = form.cleaned_data['title']
            messages.success(request, f'El cultivo: {title} ha sido creado')
            return redirect('Garden_World:crop_list')
    else:
        form = formCrop()
    return render(request, 'Garden_World/new_crop.html', {
        'form': form
    })

@login_required
def crop_list(request):
    crops = Crop.objects.order_by('title')
    context = {'crops' : crops}
    return render(request, 'Garden_World/crop_list.html', context)

@login_required
def crop_info(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)
    context = {'crop' : crop}
    return render(request, 'Garden_World/crop_info.html', context)

@login_required
def crop_edit(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)
    data = {
        'form': formCrop(instance=crop)
    }
    if request.method == 'POST':
        form = formCrop(data=request.POST, instance=crop, files=request.FILES)
        if form.is_valid():
            form.save()
            title = form.cleaned_data['title']
            messages.success(request, f'El cultivo: {title} ha sido modificado')
            return redirect('Garden_World:crop_list')
        data['form'] = formCrop()

    return render(request, 'Garden_World/crop_edit.html', data)

@login_required
def crop_delete(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)
    crop.delete()
    title = crop.title
    messages.success(request, f'El cultivo: {title} ha sido eliminado')
    return redirect('Garden_World:crop_list')