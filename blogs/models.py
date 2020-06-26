from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(null=True, max_length=255)
    content = models.CharField(null=True, max_length=255,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    """
    Represents a Blog Comment
    """
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='blogs_comments',  # "This" on the user model
        null=True
    )
    #post = models.CharField(null=True, max_length=255,)
    post = models.ForeignKey(
        Post,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='blogs_comments',  # "This" on the user model
        null=True
    )
    name = models.CharField(null=True, max_length=255,)
    email = models.CharField(null=True, max_length=255,)
    text = models.CharField(max_length=500)
    approved = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    class Meta:
        ordering = ['-created']
