from django.db import models

class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    permission = models.CharField(max_length=50)
    
    class Meta:
        db_table = "user"

    def __str__(self):
        return self.email