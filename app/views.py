"""
App views
"""
import httplib
import json

import web

import gspread
from oauth2client.client import SignedJwtAssertionCredentials

import settings

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
        sheet = self.get_google_spreadsheet()

        worksheet = sheet.get_worksheet(0)

        current_balance = worksheet.acell('B1').value
        last_expense_registered = worksheet.acell('B4').value
        return render.response(current_balance, last_expense_registered, settings.FORM_URL)

    def get_google_spreadsheet(self):
        auth_file = open('auth/google_auth.json')
        json_key = json.load(auth_file)
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
        gc = gspread.authorize(credentials)
        sheet = gc.open_by_key(json_key['sheet_id'])
        auth_file.close()
        return sheet
