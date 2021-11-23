from django.db import models


# Create your models here.
class Bucket(models.Model):
    title = models.CharField(max_length=20)
    volume = models.IntegerField()
    condition = models.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.title

    def _check_condition(self):
        if self.condition > self.volume:
            self.condition = self.volume
            return self.condition
        elif self.condition < 0:
            self.condition = 0
            return self.condition

    def fill_up_bucket(self):
        self.condition += self.volume
        self._check_condition()
        return self.condition

    def pour_out_bucket(self):
        self.condition -= self.volume
        self._check_condition()
        return self.condition

    def bucket_method(self, method, num):
        if method == f'fill up bucket {num}':
            return self.fill_up_bucket()
        elif method == f'pour out bucket {num}':
            return self.pour_out_bucket()

# class ImageBucket(models.Model):
#     volume = models.ForeignKey()
