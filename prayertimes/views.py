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

    def get(self, request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        if start_date and end_date:
            prayer_times = PrayerTime.objects.filter(start_date__lte=end_date, end_date__gte=start_date)
        else:
            today = date.today()
            prayer_times = PrayerTime.objects.filter(start_date__lte=today, end_date__gte=today)

        return render(request, "website/prayer_times.html", context={"prayer_times": prayer_times})
