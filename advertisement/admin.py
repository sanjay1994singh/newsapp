from django.contrib import admin
from .models import Advertisement,OtherAds
# Register your models here.
admin.site.register(Advertisement)
admin.site.register(OtherAds)
class AdsAdmin(admin.ModelAdmin):
    list_display = ['id', 'advert']
