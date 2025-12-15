from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        blank=True,
        related_name="followers"
    )


    def __str__(self):
        return self.username
