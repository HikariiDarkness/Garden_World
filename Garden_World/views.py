from django.shortcuts import render

# Create your views here.

def index(request):
    #Home page for Garden World
    return render(request, 'Garden_World/index.html')