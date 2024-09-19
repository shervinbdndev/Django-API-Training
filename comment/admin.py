from django.contrib import admin
from .models import Comment



class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'rate', 'created_at']
    search_fields = ['user__username', 'content']
    list_filter = ['rate', 'created_at']
    list_editable = ['rate']
    ordering = ['-created_at']
    
    

admin.site.register(Comment, CommentAdmin)