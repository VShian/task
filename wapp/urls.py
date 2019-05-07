from wapp import views
from django.urls import path

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('validate_user', views.validate_user, name='validate_user'),
]