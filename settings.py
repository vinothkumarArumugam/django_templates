INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'templatedemoapp'
]
#informing django our app name
from pathlib import Path
import os #import os module

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent #default directory
BASE_DIR2=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))        # we defined directory to the path where templates is located
TEMPLATE_DIR=os.path.join(BASE_DIR2,'templates')



#informing django templates where templates folder is located
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],            ###informing django templates where templates folder is located
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
