from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.
class Friend(models.Model):
    current_user=models.ForeignKey(User,related_name='owner',null=True,on_delete=models.CASCADE)
    users=models.ManyToManyField(User)
    @classmethod
    def makefriend(cls,current_user,new_friend):
        friendmaking,created=cls.objects.get_or_create(
        current_user=current_user
        )
        friendmaking.users.add(new_friend)
    @classmethod
    def losefriend(cls,current_user,new_friend):
        friendmaking,created =cls.objects.get_or_create(
        current_user=current_user
        )
        friendmaking.users.remove(new_friend)
