import requests


def send_email(contact_message):
    headers={
        'Access'
    }
    requests.post("https://api.web3forms.com/submit", json=contact_message)