from django.db import models
from django.utils.translation import gettext_lazy as _


class PageType(models.IntegerChoices):
    TERMS_AND_CONDITIONS = 0, _("Terms and Conditions")
    PRIVACY_POLICY = 1, _("Privacy Policy")
    COOKIE_POLICY = 2, _("Cookie Policy")
    PRICING = 3, _("Pricing")
    SUBSCRIBER_TERMS = 4, _("Subscriber Terms")
    ENTERPRISE = 5, _("Enterprise")
    DPA = 6, _("DPA")


class ContactMessageStatus(models.IntegerChoices):
    PENDING = 0, _("Pending")
    APPROVED = 1, _("Approved")
    REJECTED = 2, _("Rejected")

class PricingRequestStatus(models.IntegerChoices):
    PENDING = 0, _("Pending")
    APPROVED = 1, _("Approved")
    REJECTED = 2, _("Rejected")

class DemoRequestStatus(models.IntegerChoices):
    PENDING = 0, _("Pending")
    APPROVED = 1, _("Approved")
    REJECTED = 2, _("Rejected")