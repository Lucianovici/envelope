# -*- coding: utf-8 -*-
"""
App views
"""
import httplib
import json

import web

import settings
from services import GoogleApiService

render = web.template.render('templates/', base='base')


class EnvelopeFormView(object):
    def GET(self):
        return render.form()

    def POST(self):
        data = web.data()
        response = self.get_post_response(data)
        is_response_recorded = settings.GOOGLE_DOCS_FORM_SUCCESSFUL_RESPONSE_MESSAGE in response.read()

        json_response = {
            'isResponseRecorded': is_response_recorded,
        }

        web.header('Content-Type', 'application/json')
        return json.dumps(json_response)

    def get_post_response(self, data):
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/html"
        }
        conn = httplib.HTTPSConnection(settings.GOOGLE_DOCS_HOST)
        conn.request("POST", settings.GOOGLE_DOCS_FORM_URL, data, headers)
        response = conn.getresponse()
        return response


class EnvelopeResponseView(object):
    def GET(self):
        service = GoogleApiService(auth_json_file_path='auth/google_auth.json')

        spreadsheet = service.get_spreadsheet()
        worksheet = spreadsheet.get_worksheet(0)

        current_balance = worksheet.acell('B1').value
        last_entry_registered_amount = worksheet.acell('B2').value
        last_entry_registered_date = worksheet.acell('D2').value
        last_entry_registered_tag = worksheet.acell('F2').value

        return render.response(
            current_balance,
            last_entry_registered_amount,
            last_entry_registered_date,
            last_entry_registered_tag,
            settings.FORM_URL
        )
