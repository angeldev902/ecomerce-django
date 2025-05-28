from django.db import models
from users.models import User

class Address(models.Model):

    user = models.ForeignKey(
        User,     # Como pongo que se relacionara con el modelo de User              
        on_delete=models.CASCADE,  
        null=False,               
        blank=False, 
        related_name='addresses' # user.addresses.all() to get all address in user object   
    )

    street = models.CharField(null=False, blank=False, max_length=250)

    ext_number = models.CharField(null=False, blank=False, max_length=20)

    int_number = models.CharField(null=True, blank=True, max_length=20)

    suburb = models.CharField(null=False, blank=False, max_length=50)

    city = models.CharField(null=False, blank=False, max_length=50)

    state = models.CharField(null=False, blank=False, max_length=50)

    country = models.CharField(null=False, blank=False, max_length=50)

    zip_code = models.CharField(null=False, blank=False, max_length=5)

    comments = models.CharField(null=False, blank=False, max_length=250)

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'addresses' 
