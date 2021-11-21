from django.shortcuts import render, HttpResponse
from .models import Bucket
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BucketsSerializer


# Create your views here.
def show_buckets(request):
    buckets = Bucket.objects.all()
    return render(request, "main/show_buckets.html", {"buckets": buckets})


class BucketsAPI(APIView):
    def get(self, request):
        buckets = Bucket.objects.all()
        serializer = BucketsSerializer(buckets, many=True)
        return Response({"buckets": serializer.data})


# @csrf_exempt
# def fill_up_buckets(request):
#     if request.method == 'POST':
#         return HttpResponse(Bucket.fill_up_bucket)
