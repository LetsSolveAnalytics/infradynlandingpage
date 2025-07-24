from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductType(models.IntegerChoices):
    PRECONSTRUCTION = 0, _("Preconstruction")
    EXECUTION = 1, _("Execution")
    CONSTRUCTION_INTELLIGENCE = 2, _("Construction Intelligence")
    COLLABORATION_HUB = 3, _("Collaboration Hub")
    INTEGRATIONS = 4, _("Integrations")
    # QUALITY_AND_SAFETY = 4, _("Quality and Safety")
    
