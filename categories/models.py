from django.db import models

class Category(models.Model):

    name = models.CharField(null=False, blank=False, max_length=20, unique=True)

    code = models.CharField(null=False, blank=True, max_length=20, unique=True)

    parent_category = models.ForeignKey(
        'self',                     # related to self
        on_delete=models.CASCADE,   # what if parent is delete
        null=True,                  # it can have not parent
        blank=True,                 # it can be blank in forms
        related_name='sub_categories'  # Nombre para acceder a los hijos desde el padre  Name to access to childrens from parent
    )

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories' 
