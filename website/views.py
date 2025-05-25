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
from .forms import ContactMessageForm, RequestDemoForm, PricingRequestForm
from .models import Slider, ContactMessage, RequestDemo, PricingRequest
from coreapp.models import Testimonials, FAQ
from blogs.models import Post


# Create your views here.

class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonials.objects.filter(is_active=True)
        context['testimonial_intro'] = "What Our Clients Say!"
        context['faqs'] = FAQ.objects.filter(is_active=True)
        context['faq_intro'] = "Here are some of the most common questions we receive from our customers."
        context['sliders'] = Slider.objects.filter(is_active=True)
        context['recent_posts'] = Post.objects.filter(is_published=True).order_by('-created_at')[:6]
        return context


class AboutView(TemplateView):
    template_name = 'website/about.html'


class RequestDemoView(View):
    def get_context_data(self, **kwargs):
        return {
            'form': RequestDemoForm(),
            'faqs': FAQ.objects.filter(is_active=True),
            'faq_intro': "Here are some of the most common questions we receive from our customers."
        }

    def get(self, request):
        return render(request, 'website/request_a_demo.html', self.get_context_data())

    def post(self, request):
        form = RequestDemoForm(request.POST)
        context = self.get_context_data()

        if form.is_valid():
            data = form.cleaned_data
            demo_request = RequestDemo.objects.create(**data)
            demo_request.save()

            # Optionally send an email
            # email_utils.send_demo_request_email("team@yourcompany.com", demo_request)

            context['form'] = RequestDemoForm()
            context['submitted'] = True
        else:
            print(form.errors)
            context['form'] = form

        return render(request, 'website/request_a_demo.html', context)


class PricingRequestView(View):
    def get_context_data(self):
        return {
            'form': PricingRequestForm(),
            'faqs': FAQ.objects.filter(is_active=True),
            'faq_intro': "Here are some of the most common questions we receive from our customers."
        }

    def get(self, request):
        return render(request, 'website/pricing.html', self.get_context_data())

    def post(self, request):
        form = PricingRequestForm(request.POST)
        context = self.get_context_data()

        if form.is_valid():
            data = form.cleaned_data
            price_request = PricingRequest.objects.create(**data)
            price_request.save()

            # Optionally send an email
            # email_utils.send_demo_request_email("team@yourcompany.com", demo_request)

            context['form'] = PricingRequestForm()
            context['submitted'] = True
        else:
            print(form.errors)
            context['form'] = form

        return render(request, 'website/pricing.html', context)


class ContactView(View):
    def get(self, request):
        form = ContactMessageForm()
        return render(request, 'website/contact.html', {'form': form})

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
