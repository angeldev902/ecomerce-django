from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Brand(models.Model):

    name = models.CharField(null=False, blank=False, max_length=20)

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'brands'  # Este será el nombre exacto de la tabla en la base de datos