import csv
from django.contrib import admin, messages
from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponseRedirect
from django import forms
from io import TextIOWrapper
from .models import PrayerTime


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()


class PrayerTimeAdmin(admin.ModelAdmin):
    list_display = ('date',)  # Display fields in the admin panel

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('add/', self.admin_site.admin_view(self.add_prayer_time_view), name='add_prayer_time'),
        ]
        return custom_urls + urls

    def add_view(self, request, form_url='', extra_context=None):
        """Redirect 'Add Prayer Time' to the custom CSV upload view."""
        return HttpResponseRedirect("add/")

    def add_prayer_time_view(self, request):
        """Custom view for adding prayer times via CSV."""
        if request.method == "POST":
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = TextIOWrapper(request.FILES['csv_file'].file, encoding='utf-8')
                reader = csv.DictReader(csv_file)
                created_count = 0
                default_icon = "prayer_times/default.webp"

                for row in reader:
                    try:
                        PrayerTime.objects.update_or_create(
                            date=row['Date'],  # Use the date as a unique identifier
                            defaults={
                                'fajr_icon': default_icon,
                                'fajr_start': row['Fajr'],
                                'sunrise_icon': default_icon,
                                'sunrise_start': row['Shuruk'],
                                'dhuhr_icon': default_icon,
                                'dhuhr_start': row['Duhr'],
                                'asr_icon': default_icon,
                                'asr_start': row['Asr'],
                                'maghrib_icon': default_icon,
                                'maghrib_start': row['Maghrib'],
                                'isha_icon': default_icon,
                                'isha_start': row['Isha'],
                                'jumuah_icon': default_icon,
                                'jumuah_start': row['Duhr'] if int(row['is_friday']) == 1 else None
                            },
                        )
                        created_count += 1
                    except Exception as e:
                        self.message_user(request, f"Error processing row: {row} - {str(e)}", messages.ERROR)

                self.message_user(request, f"Successfully imported {created_count} prayer times.", messages.SUCCESS)
                return redirect('..')  # Redirect back to the admin list view

        else:
            form = CSVUploadForm()

        context = {
            **self.admin_site.each_context(request),
            'form': form,
        }
        return render(request, "admin/upload_csv_form.html", context)
