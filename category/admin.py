from django.contrib import admin

from .models import CategoryMaster
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name','created_at']

admin.site.register(CategoryMaster,CategoryAdmin)
