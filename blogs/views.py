# blogs/views.py

from django.shortcuts import render
from . import models

# Create your views here.

def home(request):
    """
    The Blog homepage

    """
    #latest_posts = models.Post.objects.published().order_by('-published')[:3]
    #context = {'latest_posts': latest_posts}
    return render(request, 'blogs/home.html', {'message': 'Hello world!'})
