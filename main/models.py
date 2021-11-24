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
        Bucket.objects.filter(volume=self.volume).update(condition=self.condition)
        # return self.condition

    def pour_out_bucket(self):
        self.condition -= self.volume
        self._check_condition()
        Bucket.objects.filter(volume=self.volume).update(condition=self.condition)
        # return self.condition

    def pour_over_bucket(self, args):
        from_bucket = Bucket.objects.filter(volume=args[0]).get()
        to_bucket = Bucket.objects.filter(volume=args[1]).get()
        sum = from_bucket.condition + to_bucket.condition
        from_bucket.condition = sum - to_bucket.volume
        from_bucket._check_condition()
        to_bucket.condition = sum - from_bucket.condition
        to_bucket._check_condition()
        Bucket.objects.filter(volume=args[0]).update(condition=from_bucket.condition)
        Bucket.objects.filter(volume=args[1]).update(condition=to_bucket.condition)

    def bucket_method(self, method, nums):
        if method == f'fill up bucket {nums[0]}':
            self.fill_up_bucket()
        elif method == f'pour out bucket {nums[0]}':
            self.pour_out_bucket()
        elif method == f'pour over from bucket {nums[0]} to bucket {nums[1]}':
            self.pour_over_bucket(nums)

# class ImageBucket(models.Model):
#     volume = models.ForeignKey()
