# myblog/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse('Welcome to MyBlog, Django project!, including Django admin modifications')
