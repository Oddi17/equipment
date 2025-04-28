from django.db import models

# Create your models here.



class Equipment(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255,unique=True)
    purchase_date = models.DateField()
    operating_hours = models.PositiveIntegerField()
    last_maintenance_date = models.DateField()
    
    

