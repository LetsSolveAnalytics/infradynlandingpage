from decouple import config

if config("DEBUG") == "False":
    from .development import *
else:
    from .production import *