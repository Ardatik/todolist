from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        verbose_name='username', max_length=50, unique=True)
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True)
    first_name = None
    last_name = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}; {self.email}"
