from django.contrib import admin
from .models import Post, Reply


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "message", "date", "author")


class ReplyAdmin(admin.ModelAdmin):
    list_display = ("post", "message", "date", "author")


admin.site.register(Reply, ReplyAdmin)
admin.site.register(Post, PostAdmin)
