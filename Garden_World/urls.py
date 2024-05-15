#Defines URL patterns for Garden_World
from django.urls import path
from . import views

app_name = 'Garden_World'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]