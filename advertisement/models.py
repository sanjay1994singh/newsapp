from django.db import models

# Create your models here.
class Advertisement(models.Model):
    ads_name = models.CharField(max_length=50,default=None)
    advert = models.ImageField(upload_to='advertisement_img', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.ads_name
    
    class Meta:
        db_table = 'advertisement'
    
