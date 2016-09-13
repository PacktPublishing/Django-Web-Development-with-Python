# -*- coding: UTF-8 -*-
from conf.dev import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(PROJECT_PATH, "myproject", "db.sqlite3"),
    }
}
