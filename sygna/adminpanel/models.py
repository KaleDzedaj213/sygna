from django.db import models
<<<<<<< HEAD
from django.core.validators import MaxValueValidator

class Client(models.Model):
    nip = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    name = models.CharField(max_length=50)
    payment = models.CharField(max_length=50)
    
    class Meta:
        db_table = "client"

    def __str__(self):
        return str(self.name)
=======

# Create your models here.
>>>>>>> 283ffdb85b50d13598a9a7b511fd083e76c38cd5
