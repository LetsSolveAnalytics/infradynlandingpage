import datetime
from datetime import date

from django.shortcuts import render
from django.views.generic import ListView

from .models import PrayerTime


# Create your views here.
class PrayerTimeView(ListView):
    """
    Retrieve prayer times based on optional start_date and end_date query parameters.
    If no parameters are provided, return today's prayer times.
    """
    template_name = 'website/prayer_times.html'
    queryset = PrayerTime.objects.all()
    context_object_name = 'prayertimes'

    def get_prayer_queryset(self):
        month = self.request.GET.get('month-select')
        queryset = self.queryset
        now = datetime.datetime.now()
        if month:
            try:
                month = int(month)
                queryset = queryset.filter(date__month=month, year=now.year)
            except ValueError:
                pass
        return queryset
