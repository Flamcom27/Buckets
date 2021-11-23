from rest_framework import serializers


class BucketsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    volume = serializers.IntegerField()
    condition = serializers.IntegerField()
