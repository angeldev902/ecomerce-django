from django.db import models
from users.models import User

class Card(models.Model):

    BRAND_CHOICES = (
        ('mastercard', 'Master Card'),
        ('visa', 'Visa'),
        ('American Express', 'American Express')
    )

    TYPES_CHOICES = (
        ('credit', 'Credit'),
        ('debit', 'Debit')
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  
        null=False,               
        blank=False, 
        related_name='cards' # user.addresses.all() to get all cards in user object   
    )

    card_id = models.CharField(max_length=20, unique=True, null=False, blank=False)

    brand = models.CharField(max_length=20, choices=BRAND_CHOICES)

    last4 = models.CharField(max_length=4, null=False, blank=False)

    card_type = models.CharField(max_length=6, choices=TYPES_CHOICES, default='credit')

    deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cards' 
    


