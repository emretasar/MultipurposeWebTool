from django.db import models


class CustomUser(models.Model):  
    username = models.CharField(max_length=20)  
    password = models.CharField(max_length=20)  
    class Meta:  
        db_table = "user"  