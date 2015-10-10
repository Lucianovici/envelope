"""
App views
"""
import web

render = web.template.render('templates/')


class EnvelopeFormView(object):
    def GET(self):
        name = 'Bob Form'
        return render.form(name)


class EnvelopeResponseView(object):
    def GET(self):
        name = 'Bob Response'
        return render.form(name)
