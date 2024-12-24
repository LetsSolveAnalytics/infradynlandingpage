from django.db import models

from coreapp.base import BaseModel


class PrayerTime(BaseModel):
    start_date = models.DateField()
    end_date = models.DateField()

    fajr_icon = models.ImageField(upload_to="prayer_times/")
    fajr_start = models.TimeField()
    fajr_iqamah_time = models.TimeField()
    fajr_end = models.TimeField(null=True, blank=True)

    dhuhr_icon = models.ImageField(upload_to="prayer_times/")
    dhuhr_start = models.TimeField()
    dhuhr_iqamah_time = models.TimeField()
    dhuhr_end = models.TimeField(null=True, blank=True)

    asr_icon = models.ImageField(upload_to="prayer_times/")
    asr_start = models.TimeField()
    asr_iqamah_time = models.TimeField()
    asr_end = models.TimeField(null=True, blank=True)

    maghrib_icon = models.ImageField(upload_to="prayer_times/")
    maghrib_start = models.TimeField()
    maghrib_iqamah_time = models.TimeField()
    maghrib_end = models.TimeField(null=True, blank=True)

    isha_icon = models.ImageField(upload_to="prayer_times/")
    isha_start = models.TimeField()
    isha_iqamah_time = models.TimeField()
    isha_end = models.TimeField(null=True, blank=True)

    jumuah_icon = models.ImageField(upload_to="prayer_times/")
    jumuah_start = models.TimeField()
    jumuah_iqamah_time = models.TimeField()
    jumuah_end = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Prayer Times from {self.start_date} to {self.end_date}"
