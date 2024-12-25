from django.db import models

from coreapp.base import BaseModel


class PrayerTime(BaseModel):
    date = models.DateField(db_index=True, unique=True)

    fajr_icon = models.ImageField(upload_to="prayer_times/", default='prayer_times/default.webp')
    fajr_start = models.TimeField()
    fajr_iqamah_time = models.TimeField(null=True,blank=True)
    fajr_end = models.TimeField(null=True, blank=True)

    dhuhr_icon = models.ImageField(upload_to="prayer_times/", default='prayer_times/default.webp')
    dhuhr_start = models.TimeField()
    dhuhr_iqamah_time = models.TimeField(null=True,blank=True)
    dhuhr_end = models.TimeField(null=True, blank=True)

    asr_icon = models.ImageField(upload_to="prayer_times/", default='prayer_times/default.webp')
    asr_start = models.TimeField()
    asr_iqamah_time = models.TimeField(null=True,blank=True)
    asr_end = models.TimeField(null=True, blank=True)

    maghrib_icon = models.ImageField(upload_to="prayer_times/", default='prayer_times/default.webp')
    maghrib_start = models.TimeField()
    maghrib_iqamah_time = models.TimeField(null=True,blank=True)
    maghrib_end = models.TimeField(null=True, blank=True)

    isha_icon = models.ImageField(upload_to="prayer_times/", default='prayer_times/default.webp')
    isha_start = models.TimeField()
    isha_iqamah_time = models.TimeField(null=True,blank=True)
    isha_end = models.TimeField(null=True, blank=True)

    jumuah_icon = models.ImageField(upload_to="prayer_times/", default='prayer_times/default.webp')
    jumuah_start = models.TimeField(null=True, blank=True)
    jumuah_iqamah_time = models.TimeField(null=True,blank=True)
    jumuah_end = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Prayer Times: {self.date}"
