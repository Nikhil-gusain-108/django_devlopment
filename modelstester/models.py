from django.db import models

# Create your models here.
class card_details(models.Model):

    url= models.CharField(max_length = 100)
    title = models.CharField(max_length = 10)
    discription = models.CharField(max_length = 100)

class courses(models.Model):
    course_name = models.CharField(max_length = 10 )
    def __str__(self):
        return self.course_name

class student(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
class teacher(models.Model):
    name = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
    