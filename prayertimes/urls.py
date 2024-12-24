from django.urls import path
from .views import PrayerTimeView

urlpatterns = [
    path('prayer-times/', PrayerTimeView.as_view(), name='prayer-times'),
]
