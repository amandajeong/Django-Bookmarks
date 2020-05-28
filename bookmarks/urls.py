from django.urls import path, include

from . import views

urlpatterns = [

    # session management
    path('register/', views.register_page, name="register"),
    path('', include('django.contrib.auth.urls')),

    # home view
    path('', views.index, name='home'),
    path('user/<str:username>/', views.user_page, name="user"),
    path('tag/<str:tag_name>/', views.tag_page),
    path('tag/', views.tag_cloud_page, name="tag_cloud"),

    # account management
    path('save/', views.bookmark_save, name="save")
]
