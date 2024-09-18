from django.contrib import admin
from .models import Comment



class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'rate', 'created_at']
    
    

admin.site.register(Comment, CommentAdmin)