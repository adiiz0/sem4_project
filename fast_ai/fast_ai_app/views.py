from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def forums(request):
    return render(request, 'forums.html')


def detail(request):
    return render(request, 'detail.html')


def posts(request):
    return render(request, 'posts.html')
