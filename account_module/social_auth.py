from django.urls import reverse

def get_social_auth_urls():
    urls = {
        'google': '/auth/login/google-oauth2/',
        'facebook': '/auth/login/facebook/',
    }
    return urls
