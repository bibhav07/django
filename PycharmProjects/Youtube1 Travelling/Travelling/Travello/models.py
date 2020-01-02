from django.db import models

# Create your models here.
class Destination(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    subtitle = models.TextField()
    price = models.TextField()
    offer = models.TextField(blank=True)
    thumb = models.ImageField(default='default.png',blank=True)


    def __str__(self):
        return self.title



