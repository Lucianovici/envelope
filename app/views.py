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


class EnvelopeHomeView(object):
    def GET(self):
        return render.home(
            web.storage({'title': 'Envelope'})
        )


class EnvelopeFormView(object):
    def GET(self):
        context = {
            'title': 'Envelope',
            'form_response_url': settings.STATS_URL
        }

        return render.form(
            web.storage(context)
        )

    def POST(self):
        data = web.data()
        response = self._get_post_response(data)
        is_response_recorded = settings.GOOGLE_DOCS_FORM_SUCCESSFUL_RESPONSE_MESSAGE in response.read()

        json_response = {
            'isResponseRecorded': is_response_recorded,
        }

        web.header('Content-Type', 'application/json')
        return json.dumps(json_response)

    def _get_post_response(self, data):
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html'
        }
        conn = httplib.HTTPSConnection(settings.GOOGLE_DOCS_HOST)
        conn.request('POST', settings.GOOGLE_DOCS_FORM_URL, data, headers)
        response = conn.getresponse()

        return response


class EnvelopeStatsView(object):
    def GET(self):
        service = GoogleApiService(auth_json_file_path='auth/google_auth.json')

        spreadsheet = service.get_spreadsheet()
        worksheet = spreadsheet.get_worksheet(0)

        overall_worksheet_values = worksheet.get_all_values()

        context = {
            'title': 'Stats',
            'current_balance': overall_worksheet_values[0][1],
            'last_amount': overall_worksheet_values[1][1],
            'last_date': overall_worksheet_values[1][3],
            'last_tag': overall_worksheet_values[1][5],
            'last_observation': overall_worksheet_values[1][6],
            'form_url': settings.FORM_URL
        }

        return render.stats(
            web.storage(context)
        )
