from django.db import models

class User(models.Model):
    #id = models.IntegerField(max_length=11, primary_key=True)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    default_password = models.CharField(max_length=50)
    permission = models.CharField(max_length=50)
    
    class Meta:
        db_table = "user"

    def __str__(self):
        return f"{self.name} {self.lastname} {self.email}"
