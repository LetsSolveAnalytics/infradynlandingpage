import datetime
from datetime import date

from django.shortcuts import render
from django.views.generic import ListView

from .models import PrayerTime


# Create your views here.
class PrayerTimeView(ListView):
    """
    Retrieve prayer times based on optional month-select query parameter.
    If no parameter is provided, return this month's prayer times.
    """
    template_name = 'website/prayer_times.html'
    queryset = PrayerTime.objects.all()
    context_object_name = 'prayertimes'

    def get_queryset(self):
        month = self.request.GET.get('month-select')
        queryset = self.queryset
        now = datetime.datetime.now()
        if month:
            try:
                month = int(month)
                if 1 <= month <= 12:
                    queryset = queryset.filter(date__month=month, date__year=now.year)
                else:
                    queryset = queryset.filter(date__month=now.month, date__year=now.year)
            except ValueError:
                queryset = queryset.filter(date__month=now.month, date__year=now.year)
        else:
            queryset = queryset.filter(date__month=now.month, date__year=now.year)
        return queryset
