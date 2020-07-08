from django.contrib import admin

# Register your models here.
from . import models

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'name',
        'email',
        'text',
        'approved',
        'created',
        'updated',
        'author',
    )
    search_fields = (
        'text',
        'name',
        'email',
    )
    list_filter = (
        'approved',
    )
admin.site.register(models.Comment, CommentAdmin)

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}

    list_filter = (
        'status',
        'topics',

    )
    list_display = (
        'title',
        'content',
        'created',
        'updated',
        'author',
        'status',
        #'comments',
    )
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name'
    )

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}
