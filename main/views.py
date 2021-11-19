from django.shortcuts import render, HttpResponse
from .models import Bucket


# Create your views here.
def show_buckets(request):
    buckets = Bucket.objects.all()
    return render(request, "main/show_buckets.html", {"buckets": buckets})
