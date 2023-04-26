from django.db import models
from django.core.validators import MaxValueValidator

class Client(models.Model):
    #nip = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    id = models.IntegerField(max_length=11)
    nip = models.IntegerField(max_length=11)
    company_name = models.CharField(max_length=50)
    billing_method = models.CharField(max_length=50)
    
    class Meta:
        db_table = "client"

    def __str__(self):
        return str(self.company_name)
