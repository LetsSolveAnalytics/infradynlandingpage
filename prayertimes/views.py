from datetime import date

from django.shortcuts import render
from django.views import View

from .models import PrayerTime


# Create your views here.
class PrayerTimeView(View):
    """
    Retrieve prayer times based on optional start_date and end_date query parameters.
    If no parameters are provided, return today's prayer times.
    """
    template_name = 'website/prayer_times.html'

    def get_prayer_queryset(self):
        month = self.request.GET.get('month-select')
        queryset = self.queryset
        if month:
            try:
                month = int(month)  
                queryset = queryset.filter(date__month=month)  
            except ValueError:
                pass  
        return queryset