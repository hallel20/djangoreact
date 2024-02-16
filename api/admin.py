from django.contrib import admin
from django.contrib.auth.models import User
from .models import Property, AgentProfile, Comment

# Register your models here.


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')


@admin.register(AgentProfile)
class AgentProfile(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment')


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
