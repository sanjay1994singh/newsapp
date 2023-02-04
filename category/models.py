from django.db import models

# Create your models here.

class CategoryMaster(models.Model):
    category_name = models.CharField(max_length=500)
    category_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table = 'category_master'