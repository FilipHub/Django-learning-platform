# /home/filipp/DNIC

import os

from SmartOS.settings import BASE_DIR, DATABASES

BASE_DIR = os.path.dirname(os.path.dirname(os.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
