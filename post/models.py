from django.db import models
from category .models import CategoryMaster
# Create your models here.

class PostMaster(models.Model):
    post_title = models.CharField(max_length=500)
    post_desc = models.TextField()
    post_img = models.ImageField(upload_to='postImage')
    post_category = models.ForeignKey(CategoryMaster,on_delete=models.CASCADE, default=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.post_title
    
    class Meta:
        db_table = 'post_master'
        