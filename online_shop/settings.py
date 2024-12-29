# ...existing code...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += [
    'social_django',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
]

# Make sure this is at the root level of settings.py
ROOT_URLCONF = 'online_shop.urls'

# Social Auth settings
SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Login/Redirect URLs
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'home'

# Social Auth Settings
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

# Google configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your_google_oauth2_key'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your_google_oauth2_secret'

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = 'your_facebook_app_id'
SOCIAL_AUTH_FACEBOOK_SECRET = 'your_facebook_app_secret'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

# ...existing code...
