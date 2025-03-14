from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View, generic
from django.views.generic import TemplateView, ListView
import requests

from coreapp import email_utils
from . import forms

from .constants import PageType
from .forms import ContactMessageForm
from .models import Slider, Service, Page, GalleryImage, EventImage, News, ContactMessage


# Create your views here.

class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(is_active=True)
        context['services'] = Service.objects.filter(is_active=True)
        return context


class IntrotoIslamView(TemplateView):
    template_name = 'website/intro-to-islam.html'

class BooksPamphletsView(TemplateView):
    template_name = 'website/books.html'

class HistoryView(TemplateView):
    template_name = 'website/history.html'

class DonateView(TemplateView):
    template_name = 'website/donate.html'

class AboutView(TemplateView):
    template_name = 'website/about.html'

class MembershipView(TemplateView):
    template_name = 'website/membership.html'

class ServiceListView(ListView):
    queryset = Service.objects.filter(is_active=True)
    template_name = 'website/services.html'
    context_object_name = 'services'

class QuranclassView(TemplateView):
    template_name = 'website/quran_classes.html'

class GalleryListView(ListView):
    queryset = GalleryImage.objects.filter(is_active=True)
    template_name = 'website/gallery.html'
    context_object_name = 'galleries'

class EventListView(ListView):
    queryset = EventImage.objects.filter(is_active=True)
    template_name = 'website/events.html'
    context_object_name = 'events'

class NewsListView(ListView):
    queryset = News.objects.filter(is_active=True)
    template_name = 'website/news.html'
    context_object_name = 'news'


class PageView(View):
    def get(self, request, path):
        try:
            page = Page.objects.get(url_path=path)
            return render(request, 'website/page.html', {'page': page})
        except ObjectDoesNotExist:
            raise Http404


class ContactView(View):
    def get(self, request):
        return render(request, 'website/contact.html')

    def post(self, request):
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            form_data.pop('captcha')
            contact_message = ContactMessage.objects.create(**form_data)
            contact_message.save()
            email_utils.send_contact_message_email("psislamilainen@gmail.com", contact_message)
        else:
            print(form.errors)
        return render(request, 'website/contact.html')