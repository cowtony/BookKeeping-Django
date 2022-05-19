from django.db import models
from django.utils import timezone

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField("Transaction date", null = False)
    time = models.TimeField("Transaction time", null = False)
    description = models.CharField(max_length=100, null = False)
    expense = models.CharField(max_length=300, null = True, default = 'Empty')
    revenue = models.CharField(max_length=300, null = True, default = 'Empty')
    asset = models.CharField(max_length=300, null = True, default = 'Empty')
    liability = models.CharField(max_length=300, null = True, default = 'Empty')
    
    def __str__(self):
        """Returns a string representation of a transaction."""
        date = timezone.localtime(self.time)
        return f"'{self.description}' logged on {date.strftime('%A, %d %B, %Y at %X')}"