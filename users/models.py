# accounts/models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        is_hod = extra_fields.pop('is_hod', False)
        is_exam_officer = extra_fields.pop('is_exam_officer', False)

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_hod = is_hod
        user.is_exam_officer = is_exam_officer
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('hod', 'HOD'),
        ('exam_officer', 'Exam Officer'),
    )

    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='hod')

    objects = CustomUserManager()

    # Remove 'username' field from the model
    username = None

    USERNAME_FIELD = 'email'  # Use the email field as the unique identifier

    REQUIRED_FIELDS = []  # Remove 'email' from REQUIRED_FIELDS

    def __str__(self):
        return self.email
