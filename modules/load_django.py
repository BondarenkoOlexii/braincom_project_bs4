"""
Initialisation Django for start parsing besides Django-project
"""

import os
import sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.insert(
    0,
    os.path.join(BASE_DIR, "braincom_project"),
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "braincom_project.settings")

django.setup()