# -*- coding: UTF-8 -*-
from conf.dev import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(PROJECT_PATH, "myproject", "db.sqlite3"),
    }
}

LAST_FM_API_KEY = "749ab9ade5d1a46f5561f78104e7182c"  # enter your Last.fm API key