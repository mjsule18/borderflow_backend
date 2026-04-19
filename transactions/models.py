from django.db import models
from accounts.models import User


class Transaction(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver_name = models.CharField(max_length=255)
    receiver_country = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency_from = models.CharField(max_length=3)
    currency_to = models.CharField(max_length=3)
    exchange_rate = models.DecimalField(max_digits=12, decimal_places=6)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    
# Create your models here.
