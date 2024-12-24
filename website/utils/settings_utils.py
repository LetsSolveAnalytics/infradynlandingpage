from ..models import GlobalSettings


def get_settings():
    return GlobalSettings.objects.first()
