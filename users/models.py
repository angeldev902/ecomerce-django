# users/models.py
from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    first_name = models.CharField(max_length=255)

    last_name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(10)])

    password = models.CharField(max_length=128)

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}".strip()
    class Meta:
        db_table = 'users'  # Este será el nombre exacto de la tabla en la base de datos
