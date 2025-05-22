from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductType(models.IntegerChoices):
    PRECONSTRUCTION = 0, _("Preconstruction")
    PROJECTDELIVERY = 1, _("ProjectDelivery")
    ANALYTICS = 2, _("Analytics")
    COLLABORATION = 3, _("CollaborationAndCommunication")
