from django.urls import path
from main import views

urlpatterns = [
    path('', views.show_buckets,),
    path('api/', views.BucketsAPI.as_view()),

    # path('', views.fill_up_buckets, name='home'),
]
