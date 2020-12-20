from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from groups.models import Group

User = get_user_model()

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(
        Group, related_name='posts', on_delete=models.CASCADE,
        blank=True, null=True)
    image=models.ImageField(upload_to='profiles',blank=True)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)

    def __str__(self):
        return self.message
    def like(self):
        self.likes+=1
        self.save()
    def dislike(self):
        self.dislikes+=1
        self.save()

    def save(self, *args, **kwargs):
        self.message_html = self.message
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'posts:single',
            kwargs={
                'username': self.user.username,
                'pk': self.pk
            }
        )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message', 'created_at']
