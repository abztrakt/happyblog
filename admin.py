from abztrakt.happyblog.models import Post, Tag
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    fields = ('slug', 'title', 'date', 'body', 'image', 'assoc_tags')
    list_display = ('title', 'author', 'date')
    date_hierarchy = 'date'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)

admin.site.register(Tag)
