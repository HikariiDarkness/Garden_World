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
    path('new_crop/', views.new_crop, name='new_crop'),
    path('crop_list/', views.crop_list, name='crop_list'),
    path('crop_list/<int:crop_id>/', views.crop_info, name='crop_info'),
    path('crop_edit/<int:crop_id>/', views.crop_edit, name='crop_edit'),
    path('crop_delete/<int:crop_id>/', views.crop_delete, name='crop_delete'),
    path('login/', LoginView.as_view(template_name='Garden_World/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Garden_World/logout.html'), name='logout'),
] 