from django.contrib import admin
from .models import book
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','book','text','datetime_create',)


admin.site.register(book)
# admin.site.register(Comment,CommentAdmin)



