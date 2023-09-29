from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Modified model User."""

    email = models.EmailField(
        "email address",
        help_text="User's email address",
        unique=True,
        error_messages={"unique": "A user with that email already exists."},
    )

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username
