from django.db import models

class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    isAdmin = models.BooleanField(default=False)
    
    class Meta:
        db_table = "user"
