from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    image = models.ImageField(upload_to='upload')
    description = models.CharField(max_length=50)
    price = models.FloatField()
    user = models.ForeignKey(User, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
