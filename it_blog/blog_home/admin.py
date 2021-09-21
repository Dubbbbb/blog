from django.contrib import admin
from blog_home.models import Tag, Post, Comment

class AdminTag(admin.ModelAdmin):
    list_display = ("name",)


class AdminPost(admin.ModelAdmin):
    list_display = ("title", "author")

class AdminComment(admin.ModelAdmin):
    list_display = ("post", "author")


admin.site.register(Tag, AdminTag)
admin.site.register(Post, AdminPost)
admin.site.register(Comment, AdminComment)