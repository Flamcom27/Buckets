from django.urls import path
from main import views

urlpatterns = [
    path('', views.BucketsView.as_view()),
    path('api/', views.BucketsAPI.as_view()),

    # path('', views.fill_up_buckets, name='home'),
]
