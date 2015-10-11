"""
App views
"""
import web

render = web.template.render('templates/', base='base')


class EnvelopeFormView(object):
    def GET(self):
        action_url = 'https://docs.google.com/forms/d/1p9SXHNFLTkcbnMTbBLoftJMM1NrR5WChE2qOEaY92tk/formResponse'
        return render.form(action_url)


class EnvelopeResponseView(object):
    def GET(self):
        return render.response()
