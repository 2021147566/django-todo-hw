# tweet/models.py
from django.db import models
from user.models import UserModel


# Create your models here.
class PostModel(models.Model):
    class Meta:
        db_table = "post"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    title = models.TextField(max_length=256)
    content = models.TextField(max_length=256)