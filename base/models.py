from django.db import models

# Create your models here.

class Record(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=30)

    class Meta:
        ordering = ('name',)
