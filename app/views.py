# -*- coding: utf-8 -*-
"""
App views
"""
import httplib
import json
import urlparse

import web
from utils import ConfirmationPageParser

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
        data = web.input()
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
        html_response = response.read()

        json_response = {
            'is_entry_recorded': ConfirmationPageParser.is_entry_recorded_for(html_response),
            'edit_last_response_params': ConfirmationPageParser.get_edit_last_response_form_params(html_response),
        }

        web.header('Content-Type', 'application/json')
        return json.dumps(json_response)

    def _get_post_response(self, data):
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html'
        }

        action_url = settings.FORM_ACTION_URL
        params_dict = urlparse.parse_qs(data)

        edit_last_response_params = params_dict.get('edit-last-response-params', '')

        if edit_last_response_params:
            action_url += edit_last_response_params

        conn = httplib.HTTPSConnection(settings.GOOGLE_DOCS_HOST)
        conn.request('POST', action_url, data, headers)

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
            'last_observations': overall_worksheet_values[1][6],
            'form_url': settings.FORM_URL,
        }

        context.update({
            'form_edit_last_response_params': self._get_edit_last_response_params(context)
        })

        return render.stats(
            web.storage(context)
        )

    def _get_edit_last_response_params(self, context):
        return 'amount=%s&tag=%s&observations=%s' % (
            context['last_amount'],
            context['last_tag'],
            context['last_observations'],
        )
