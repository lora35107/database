from django.db import models

class Student(models.Model):
    Jina = models.CharField(max_length=50, blank=True, null=False)
    Baruapepe = models.EmailField(max_length=50, blank=True, null=False)
    Umri = models.IntegerField(max_length=50, blank=True, null=False)
    Jinsia = models.CharField(max_length=50, blank=True, null=False)

def __str__(self):
