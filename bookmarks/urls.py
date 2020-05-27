from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('', include('django.contrib.auth.urls')),

    path('', views.index, name='home'),
    path('user/<str:username>', views.userPage, name="user"),
]
