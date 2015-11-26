# -*- coding: utf-8 -*-
"""
App Index - main entry point.
"""
import web
import settings

urls = (
    settings.FORM_URL, "views.EnvelopeFormView",
    settings.STATS_URL, "views.EnvelopeStatsView",
)

app = web.application(urls, globals())

# Get the WSGI app, to be used with gunicorn.
wsgi_app = app.wsgifunc()

if __name__ == "__main__":
    # Use as a standalone python simple server, for debugging.
    # python index.py
    app.run()
