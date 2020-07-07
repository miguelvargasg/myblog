# myblog/views.py

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Welcome to MyBlog, Django project!, including Django admin modifications')
