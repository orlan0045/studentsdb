import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST' : 'localhost',
        'USER' : 'root',
        'PASSWORD' : '13579',
        'NAME' : 'students_db',
    }
}