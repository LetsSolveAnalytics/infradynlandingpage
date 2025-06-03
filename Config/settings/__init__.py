from decouple import config

if config("ENV_TYPE") == "development":
    from .development import *
elif config("ENV_TYPE") == "production":
    from .production import *
else:
    raise ValueError("ENV_TYPE must be 'development' or 'production'")