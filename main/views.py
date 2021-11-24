from django.shortcuts import render
from .models import Bucket
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BucketsSerializer
from django.views.generic import TemplateView


# Create your views here.
# def show_buckets(request):
#     buckets = Bucket.objects.all()
#     return render(request, "main/show_buckets.html", {"buckets": buckets})


class BucketsView(TemplateView, Bucket):
    template_name = "main/show_buckets.html"
    buckets = Bucket.objects.all()
    # bucket_5 = Bucket.objects.filter(volume=5).get()
    # bucket_3 = Bucket.objects.filter(volume=3).get()

    def get(self, request):
        self.buckets = Bucket.objects.all()
        return render(request, self.template_name, {
            "buckets": self.buckets
        })

    def post(self, request):
        method = request.POST["bucket"]
        nums = [int(i) for i in method.split() if i.isdigit()]
        bucket = Bucket.objects.filter(volume=nums[0]).get()
        # volume_of_bucket = int(method[-1])
        # bucket = Bucket.objects.filter(volume=volume_of_bucket).get()
        # print(nums)
        bucket.bucket_method(method, nums)
        # Bucket.objects.filter(volume=volume_of_bucket).update(condition=cur_con)
        self.buckets = Bucket.objects.all()
        return render(request, self.template_name, {
            "buckets": self.buckets
        })


# def fill_up(request):
#     if request.method == 'POST':
#
#     return render(request, "main/show_buckets.html")


class BucketsAPI(APIView):
    def get(self, request):
        buckets = Bucket.objects.all()
        serializer = BucketsSerializer(buckets, many=True)
        return Response({"buckets": serializer.data})

# @csrf_exempt
# def fill_up_buckets(request):
#     if request.method == 'POST':
#         return HttpResponse(Bucket.fill_up_bucket)
