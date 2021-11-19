from django.db import models


# Create your models here.
class Bucket(models.Model):
    volume = models.IntegerField()
    condition = models.IntegerField()

    def __str__(self):
        self.name = f'Bucket {self.volume} Liters'
        return self.name

    def check_condition(self):
        if self.condition > self.volume:
            self.condition = self.volume
            return self.condition
        elif self.condition < 0:
            self.condition = 0
            return self.condition
