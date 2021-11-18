from django.db import models


# Create your models here.
class Bucket(models.Model):
    volume = models.IntegerField()
    condition = models.IntegerField()

    def __str__(self):
        self.name = f'Bucket {self.volume} Liters'
        return self.name
