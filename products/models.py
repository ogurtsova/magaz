from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='upload')
    description = models.CharField(max_length=50)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)




