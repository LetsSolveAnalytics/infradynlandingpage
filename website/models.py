from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from parler.models import TranslatedFields

from coreapp.base import BaseModel, BaseTranslateModel
from website.constants import ContactMessageStatus


# Create your models here.


class Slider(BaseTranslateModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=250),
        subtitle=models.CharField(max_length=200),
        btn_text=models.CharField(max_length=120, null=True, blank=True)
    )
    image = models.ImageField(upload_to='website/sliders/')
    btn_url = models.CharField(max_length=150, null=True, blank=True)
    enable_btn = models.BooleanField(default=False)
    position = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}"


class Solution(BaseTranslateModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=120),
        desc=models.TextField()
    )
    image = models.ImageField(upload_to='website/services/')
    position = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}"

class GlobalSettings(BaseTranslateModel):
    site_name = models.CharField(max_length=100)
    site_logo = models.ImageField(upload_to="website/logo/", default="default.png")
    site_url = models.CharField(max_length=100)

    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about_us = models.CharField(max_length=100)
    google_map = models.TextField(null=True, blank=True)

    bank_name = models.CharField(max_length=100, null=True, blank=True)
    branch_name = models.CharField(max_length=100, null=True, blank=True)
    account_name = models.CharField(max_length=100, null=True, blank=True)
    account_iban = models.CharField(max_length=100, null=True, blank=True)
    bank_bic = models.CharField(max_length=100, null=True, blank=True)
    bank_swift_code = models.CharField(max_length=100, null=True, blank=True)

    facebook_url = models.CharField(max_length=100, null=True, blank=True)
    instagram_url = models.CharField(max_length=100, null=True, blank=True)
    whatsapp_url = models.CharField(max_length=100, null=True, blank=True)
    youtube_url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.site_name


class ContactMessage(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=600)
    status = models.SmallIntegerField(choices=ContactMessageStatus.choices, default=ContactMessageStatus.PENDING)

    def __str__(self):
        return f"{self.name}: {self.subject} - {self.status}"

class RequestDemo(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    has_company = models.CharField(max_length=10)
    solution = models.CharField(max_length=100)
    subscribe = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class PricingRequest(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    annual_volume = models.CharField(max_length=20)
    company_type = models.CharField(max_length=100)
    subscribe = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Testimonial(BaseModel):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='website/home/')