from django.db import models


# Create your models here.
class Bucket(models.Model):
    title = models.CharField(max_length=20)
    volume = models.IntegerField()
    condition = models.IntegerField()

    def __str__(self):
        return self.title

    def check_condition(self):
        if self.condition > self.volume:
            self.condition = self.volume
            return self.condition
        elif self.condition < 0:
            self.condition = 0
            return self.condition

    def fill_up_bucket(self):
        self.condition += self.volume
        self.check_condition()
        return self.condition

# class ImageBucket(models.Model):
#     volume = models.ForeignKey()
