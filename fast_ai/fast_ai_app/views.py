from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Author, Category, Post
from .utils import update_views

# Create your views here.


def forums(request):
    return render(request, 'forums.html', {})


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post":post
    }
    update_views(request, post)

    return render(request, 'detail.html', context)


def posts(request):
    return render(request, 'posts.html')
