#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

urls = ("/.*", "Hello")

app = web.application(urls, globals())
render = web.template.render('app/templates/')

class Hello:
    def GET(self):
        name = 'Bob'
        return render.form(name)


if __name__ == "__main__":
    # web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app = web.application(urls, globals())
    app.run()
