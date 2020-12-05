from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
class UserPicture(models.Model):
        user = models.OneToOneField(User, on_delete = models.CASCADE,related_name="profs")
        picture = models.ImageField(upload_to='profiles/',blank=True)
