from django.contrib import admin
from .models import PostMaster
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title','created_at']
    
admin.site.register(PostMaster,PostAdmin)
