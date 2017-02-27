from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    profile_image = models.ImageField(upload_to='user')

    def __str__(self):
        return '{} {}'.format(
            self.last_name,
            self.first_name,
        )
