#Defines URL patterns for Garden_World
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'Garden_World'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('homesite/', views.homesite, name='homesite'),
    path('login/', LoginView.as_view(template_name='Garden_World/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Garden_World/logout.html'), name='logout')
] 