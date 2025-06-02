from decouple import config

if config("DEBUG") == "True":
    from .development import *
else:
    from .production import *
