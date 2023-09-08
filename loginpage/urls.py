from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login', views.handlelogin, name='handlelogin'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.handlelogout, name='handlelogout')
]
