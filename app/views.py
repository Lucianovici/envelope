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
            'form_amount_input_name': settings.FORM_AMOUNT_INPUT_NAME,
            'form_tag_input_name': settings.FORM_TAG_INPUT_NAME,
            'form_observations_input_name': settings.FORM_OBSERVATIONS_INPUT_NAME,
            'form_tag_options': self._get_form_tag_options(),
            'form_response_url': settings.STATS_URL,
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
        conn.request('POST', settings.FORM_ACTION_URL, data, headers)
        response = conn.getresponse()

        return response

    def _get_form_tag_options(self):
        return [tag.strip() for tag in settings.FORM_TAG_OPTIONS.split(',')]


class EnvelopeStatsView(object):
    def GET(self):
        service = GoogleApiService(auth_json_file_path=settings.GOOGLE_DOCS_AUTH_JSON_FILE_PATH)

        spreadsheet = service.get_spreadsheet(settings.RESPONSES_SPREADSHEET_ID)
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
