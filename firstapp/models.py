from django.db import models
from django.utils import timezone
# Create your models here.
class cars(models.Model):
    cars =[("MS","marutisizuki"),("NA","nano"),("TA","tata")]
    car_names =models.CharField(max_length =2,choices=cars)
    user_name = models.CharField(max_length = 100)
    date = models.DateField(default = timezone.now)
