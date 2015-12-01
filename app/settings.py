# -*- coding: utf-8 -*-
"""
Global settings.
"""
import os
from os.path import dirname, abspath, join

APP_ROOT_PATH = dirname(dirname(abspath(__file__)))

FORM_URL = os.getenv("ENVELOPE_FORM_URL", "/form")
STATS_URL = os.getenv("ENVELOPE_STATS_URL", "/stats")

FORM_TAG_OPTIONS = os.getenv(
    "ENVELOPE_FORM_TAG_OPTIONS",
    """
    Pocket Money - John,
    Pocket Money - Jade,
    Shopping,
    Restaurants,
    Sports,
    Doctor,
    Donation,
    Miscellaneous,
    Load
    """
)

FORM_AMOUNT_INPUT_NAME = os.getenv("ENVELOPE_FORM_AMOUNT_INPUT_NAME", "entry.1502227107")
FORM_TAG_INPUT_NAME = os.getenv("ENVELOPE_FORM_TAG_INPUT_NAME", "entry.618861186")
FORM_OBSERVATIONS_INPUT_NAME = os.getenv("ENVELOPE_FORM_OBSERVATIONS_INPUT_NAME", "entry.32186776")

GOOGLE_DOCS_AUTH_JSON_FILE_PATH = os.getenv(
    "ENVELOPE_AUTH_JSON_FILE_PATH", join(APP_ROOT_PATH, "app/auth/credentials/envelope_auth.json")
)

GOOGLE_DOCS_FORM_SUCCESSFUL_RESPONSE_MESSAGE = os.getenv(
    "ENVELOPE_DOCS_FORM_SUCCESSFUL_RESPONSE_MESSAGE", "Your response has been recorded"
)

# Go to your live google form and inspect the <form> element. Use its `action` here.
GOOGLE_DOCS_HOST = "docs.google.com"
FORM_ACTION_URL = os.getenv(
    "ENVELOPE_FORM_ACTION_URL", "/forms/d/1p9SXHNFLTkcbnMTbBLoftJMM1NrR5WChE2qOEaY92tk/formResponse"
)

# Use your response google spreadsheet linked with the form.
RESPONSES_SPREADSHEET_ID = os.getenv(
    "ENVELOPE_RESPONSES_SPREADSHEET_ID", "1JdA9__NEHCuqnt6hKvidM7rHIalme-G0Z_NcPHsi6_4"
)

# Local settings override
try:
    from settings_local import *
except ImportError:
    pass

