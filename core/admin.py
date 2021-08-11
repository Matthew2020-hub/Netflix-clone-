from django.contrib import admin
from .models import(
    Post,
    Comment,
    Like,
    Follow,
)

class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('text', 'users', 'created_on', 'updated_on')


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)
# Register your models here.
