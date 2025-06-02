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
from customers.models import Customer
from . import forms

from .constants import PageType
from .forms import ContactMessageForm, RequestDemoForm, PricingRequestForm
from .models import Slider, ContactMessage, RequestDemo, PricingRequest
from coreapp.models import Testimonials, FAQ
from blogs.models import Post
import logging

logger = logging.getLogger(__name__)


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
        context['customers'] = Customer.objects.filter(is_published=True)
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
            form_data = form.cleaned_data
            try:
                demo_request = RequestDemo.objects.create(**form_data)
                demo_request.save()
                print("Saving request successful.")
                email_utils.send_demo_request_message_email("lynalysis@gmail.com", demo_request)
                print("Email function called successfully.")
            except Exception as e:
                print("Error creating request or sending email:", e)

            context['form'] = RequestDemoForm()
            context['submitted'] = True
        else:
            print("Form is invalid:", form.errors)

        return render(request, 'website/request_a_demo.html', context)

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
            email_utils.send_contact_message_email("lynalysis@gmail.com", contact_message)
        else:
            print(form.errors)
        return render(request, 'website/contact.html')

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
            form_data = form.cleaned_data
            try:
                pricing_request = PricingRequest.objects.create(**form_data)
                pricing_request.save()
                print("Saving request successful.")
                email_utils.send_price_request_message_email("lynalysis@gmail.com", pricing_request)
                print("Email function called successfully.")
            except Exception as e:
                print("Error creating request or sending email:", e)

            context['form'] = PricingRequestForm()
            context['submitted'] = True
        else:
            print("Form is invalid:", form.errors)

        return render(request, 'website/pricing.html', context)
