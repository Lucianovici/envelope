# -*- coding: utf-8 -*-
"""
Global settings.
"""
import os
from os.path import dirname, abspath, join

APP_ROOT_PATH = dirname(dirname(abspath(__file__)))

FORM_URL = os.getenv("ENVELOPE_FORM_URL", "/form")
STATS_URL = os.getenv("ENVELOPE_RESPONSE_URL", "/stats")

FORM_TAG_OPTIONS = os.getenv("ENVELOPE_FORM_TAG_OPTIONS", "TBD")

GOOGLE_DOCS_AUTH_JSON_FILE_PATH = os.getenv(
    "ENVELOPE_AUTH_JSON_FILE_PATH", join(APP_ROOT_PATH, "app/auth/google_auth.json")
)

GOOGLE_DOCS_FORM_SUCCESSFUL_RESPONSE_MESSAGE = os.getenv(
    "ENVELOPE_DOCS_FORM_SUCCESSFUL_RESPONSE_MESSAGE", "Your response has been recorded"
)

GOOGLE_DOCS_HOST = "docs.google.com"
GOOGLE_DOCS_FORM_URL = os.getenv(
    "ENVELOPE_DOCS_FORM_URL", "/forms/d/1p9SXHNFLTkcbnMTbBLoftJMM1NrR5WChE2qOEaY92tk/formResponse"
)
