from django.db import models
import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    desciption = models.TextField()
    image = models.ImageField(upload_to = 'blog/images')
    #deata manera le descimos al programa que si no ponemos una fecha en automatico ponga la fecha actual 
    date = models.DateField(datetime.date.today) 

