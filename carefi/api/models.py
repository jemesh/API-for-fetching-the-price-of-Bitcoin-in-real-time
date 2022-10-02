from django.db import models
from . import price
# Create your models here.
class priceofbitcoin(models.Model):
    price=models.CharField(max_length=200)
    dateandtime=models.DateTimeField(auto_now_add=True)