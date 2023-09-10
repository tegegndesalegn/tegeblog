from django.db import models
from datetime import datetime

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    post_image = models.ImageField(null=True, blank=True , upload_to="images/")
    
    

