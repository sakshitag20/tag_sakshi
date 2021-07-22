# Register your models here.
from django.contrib import admin
from .models.post import Post
from .models.user import User


class AdminUser(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','password','username']

class AdminPost(admin.ModelAdmin):
    list_display = ['user','text','created_at','updated_at']

admin.site.register(User, AdminUser)
admin.site.register(Post, AdminPost)