# -*- coding: utf-8 -*-
"""
Global settings.
"""
import os

FORM_URL = os.getenv("ENVELOPE_FORM_URL", "/form")
STATS_URL = os.getenv("ENVELOPE_RESPONSE_URL", "/stats")

FORM_TAG_OPTIONS = os.getenv("ENVELOPE_FORM_TAG_OPTIONS", "TBD")

GOOGLE_DOCS_FORM_SUCCESSFUL_RESPONSE_MESSAGE = os.getenv(
    "ENVELOPE_DOCS_FORM_SUCCESSFUL_RESPONSE_MESSAGE", "Your response has been recorded"
)

GOOGLE_DOCS_HOST = "docs.google.com"
GOOGLE_DOCS_FORM_URL = os.getenv(
    "ENVELOPE_DOCS_FORM_URL", "/forms/d/1p9SXHNFLTkcbnMTbBLoftJMM1NrR5WChE2qOEaY92tk/formResponse"
)
