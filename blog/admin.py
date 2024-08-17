from django.contrib import admin

# Register your models here.

from blog.models import Category, Comment, Post


class CategoyAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoyAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
