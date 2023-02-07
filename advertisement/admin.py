from django.contrib import admin
from .models import Advertisement
# Register your models here.
admin.site.register(Advertisement)
class AdsAdmin(admin.ModelAdmin):
    list_display = ['id', 'advert']
