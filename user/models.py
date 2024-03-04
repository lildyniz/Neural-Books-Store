from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.username
