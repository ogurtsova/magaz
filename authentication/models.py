from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    userpic = models.ImageField(upload_to='upload')
    user = models.OneToOneField(User)
