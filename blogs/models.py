from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q


# Create your models here.
'''
class CommentManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(approved='approved')
'''
class CommentQuerySet(models.QuerySet):
    def approved(self):
        return self.filter(approved=self.model.APPROVED)
    def notapproved(self):
        return self.filter(approved=self.model.NOTAPPROVED)

class PostQuerySet(models.QuerySet):
    def find(self):
        expression = 'django'
        return self.filter(Q(title__icontains=expression) | Q(content__icontains=expression))

class Topic(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True  # No duplicates!
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']


class Post(models.Model):
    topics = models.ManyToManyField(
        Topic,
        related_name='blogs_posts'
    )

    slug = models.SlugField(
        null=False,
        help_text='The date & time this article was published',
        unique_for_date='published',
    )
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text='The date & time this article was published'
    )

    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post publicly visible',
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # The Django auth user model
        on_delete=models.PROTECT,  # Prevent posts from being deleted
        related_name='blogs_posts',  # "This" on the user model
        null=False,
    )
    title = models.CharField(null=True, max_length=255)
    content = models.CharField(null=True, max_length=255,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title


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
    #approved = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    class Meta:
        ordering = ['-created']

    APPROVED = 'approved'
    NOTAPPROVED = 'notapproved'
    APPROVED_CHOICES = [
        (APPROVED, 'approved'),
        (NOTAPPROVED, 'notapproved')
    ]

    approved = models.CharField(
        max_length=20,
        choices=APPROVED_CHOICES,
        default=APPROVED,
        help_text='Set to "approved" to make this post publicly visible'
    )

    #approved = models.BooleanField()
    objects = CommentQuerySet.as_manager()
    #objects = CommentManager()
