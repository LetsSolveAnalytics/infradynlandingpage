from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomerType(models.IntegerChoices):
    GENERALCONTRACTORS = 0, _("GeneralContractors")
    SUBCONTRACTORS = 1, _("Subcontractors")
    EPCMs = 2, _("EPCM")
    OWNERS = 3, _("Owners")
