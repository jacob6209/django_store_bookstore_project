from django.contrib import admin
from .models import book
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','bok','text','datetime_create','is_active','recommend')


admin.site.register(book)
# admin.site.register(Comment,CommentAdmin)



