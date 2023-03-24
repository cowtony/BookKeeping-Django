from django.db import models

class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField("Date", null = False)
    EUR = models.FloatField(null = False, default = 1.0)
    USD = models.FloatField(null = False, default = 1.0)
    CNY = models.FloatField(null = False, default = 1.0)
    GBP = models.FloatField(null = False, default = 1.0)
    

class CurrencyType(models.Model):
    pass
