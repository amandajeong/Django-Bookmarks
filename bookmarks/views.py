from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import *
from .models import *


# Create your views here.
def index(request):
    context = {
        'head_title': 'Django Bookmark',
        'page_title': 'Welcome to Django Bookmark',
        'page_body': 'Save and share bookmarks!'
    }
    return render(request, 'bookmarks/home.html', context)


def userPage(request, username):
    user_id = get_object_or_404(User, username=username)
    bookmarks = user.bookmark_set.all()

    context = {
        'username': user_id,
        'bookmarks': bookmarks
    }

    return render(request, 'bookmarks/user.html', context)


def registerPage(request):
    form = RegisterForm

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def logoutPage(request):
    context = {}
    return render(request, 'registration/logout.html', context)