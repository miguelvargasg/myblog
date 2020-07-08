# blogs/views.py

from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    latest_posts = models.Post.objects.all()
    # Add as context variable "latest_posts"
    context = {'latest_posts': latest_posts}
    return render(request, 'blogs/home.html', context)
    #return render(request, 'blogs/home.html', {'message': 'Hello world!'})
