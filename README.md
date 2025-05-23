# PSIY Website
[![Django CI/CD Pipeline](https://github.com/PohjoisSuomenIslamilainenYhdyskunta/PSIY/actions/workflows/deploy.yml/badge.svg)](https://github.com/PohjoisSuomenIslamilainenYhdyskunta/PSIY/actions/workflows/deploy.yml)


## Setup instructions


### Requirements

- Python 3.11
- PostgreSQL 16
- Pip
- venv


### Steps

1. Create virtual environment
    ```
    python venv venv
    ```
2. Activate virtual environment
    ```
    source venv/bin/activate
    ```
3. Install the libraries
    ```
    pip install -r requirements/development.txt
    ```
4. Edit the .env file and update the following values
    ```
   SECRET_KEY=YOUR_SECRET_KEY
    ALLOWED_HOSTS=HOSTNAME1.COM, HOSTNAME2.COM
    DEBUG=True
    
    DB_NAME=psiy
    DB_USER=admin
    DB_PASSWORD=@@@admin@@@
    DB_HOST=localhost
    DB_PORT=5433
    
    CACHE_LOCATION=YOUR_CACHE_LOCATION
    
    
    EMAIL_HOST=mail.yourdomain.com
    EMAIL_PORT=465
    EMAIL_HOST_USER=your_email_address
    EMAIL_HOST_PASSWORD=your_email_password
    
    
    STATIC_ROOT=/path/to/static/files
    MEDIA_ROOT=/path/to/media/files
    MEDIA_HOST=https://backend.yourdomain.com
    ```
   
5. Generate Migration
    ```
    python manage.py makemigrations
    ```
6. Migrate database
    ```
    python manage.py migrate
    ```
7. Run the project
    ```
    python manage.py runserver
    ```

### How to know the username and the password of the admin:

```bash
python manage.py shell 
from coreapp.models import User
User.objects.filter(is_superuser=True).values('email') # shows the list of emails
User.objects.get(email="admin_email@email.com").set_password("YournewPassword")
```
