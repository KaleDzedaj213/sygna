from django.db import models
from django.core.validators import MaxValueValidator

class Client(models.Model):
    #id = models.IntegerField(max_length=11, primary_key=True)
    nip = models.CharField(max_length=20)
    company_name = models.CharField(max_length=200)
    billing_method = models.CharField(max_length=50)
    
    class Meta:
        db_table = "client"

    def __str__(self):
        return str(f"{self.nip}, {self.company_name}")
