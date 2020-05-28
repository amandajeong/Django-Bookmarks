from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


def user_page(request, username):
    user_id = get_object_or_404(User, username=username)
    bookmarks = user_id.bookmark_set.order_by('-id')

    context = {
        'username': user_id,
        'bookmarks': bookmarks,
        'show_tags': True
    }

    return render(request, 'bookmarks/user.html', context)


def register_page(request):
    form = RegisterForm

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


@login_required(login_url='/login/')
def bookmark_save(request):
    form = BookmarkSaveForm()

    if request.method == "POST":
        form = BookmarkSaveForm(request.POST)
        if form.is_valid():

            # extract url or create new
            link, dummy = Link.objects.get_or_create(
                url=form.cleaned_data['url']
            )

            # extract bookmark or create new
            bookmark, created = Bookmark.objects.get_or_create(
                user_id=request.user,
                link_id=link
            )

            # edit bookmark title
            bookmark.title = form.cleaned_data['title']

            # if bookmark is edited, erase previous tags
            if not created:
                bookmark.tag_set.clear()

            # create new tags
            tag_names = form.cleaned_data['tags'].split()
            for tag_name in tag_names:
                tag, dummy = Tag.objects.get_or_create(name=tag_name)
                bookmark.tag_set.add(tag)

            # save bookmark
            bookmark.save()
            return_url = '/user/' + request.user.username
            return redirect(return_url)

    context = {'form': form}
    return render(request, 'bookmarks/bookmark_save.html', context)


def tag_page(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    bookmarks = tag.bookmarks.order_by('-id')
    context = {
        'bookmarks': bookmarks,
        'tag_name': tag_name,
        'show_tags': True,
        'show_user': True
    }
    return render(request, 'bookmarks/tag.html', context)


def tag_cloud_page(request):
    MAX_WEIGHT = 5
    tags = Tag.objects.order_by('name')

    # Calculate tag, min and max ounts
    min_count = max_count = tags[0].bookmarks.count()
    for tag in tags:
        tag.count = tag.bookmarks.count()
        if tag.count < min_count:
            min_count = tag.count
        if max_count < tag.count:
            max_count = tag.count

    # Calculate count range. Avoid dividing by zero
    tag_range = float(max_count - min_count)
    if tag_range == 0.0:
        tag_range = 1.0

    # Calculate tag weights
    for tag in tags:
        tag.weight = int(
            MAX_WEIGHT * (tag.count - min_count) / tag_range
        )

    context = {'tags': tags}

    return render(request, 'bookmarks/tag_cloud.html', context)

