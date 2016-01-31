# -*- coding: utf-8 -*-
"""
App views
"""
import httplib
import json
import urlparse

import web

import settings
from services import GoogleApiService, EditLastEntryService
from utils import ConfirmationPageParser

render = web.template.render('templates/', base='base')


class EnvelopeHomeView(object):
    def GET(self):
        return render.home(
            web.storage({'title': 'Envelope'})
        )


class EnvelopeFormView(object):
    def GET(self):
        return render.form(
            web.storage(self.get_context())
        )

    def _get_base_context(self):
        return {
            'stats_url': settings.STATS_URL,
            'form_url': settings.FORM_URL,
            'form_amount_input_name': settings.FORM_AMOUNT_INPUT_NAME,
            'form_tag_input_name': settings.FORM_TAG_INPUT_NAME,
            'form_observations_input_name': settings.FORM_OBSERVATIONS_INPUT_NAME,
            'form_tag_options': self._get_form_tag_options(),
        }

    def _get_form_values_context(self):
        get_params = web.input()

        return {
            'form_amount_input_value': get_params.get(settings.FORM_AMOUNT_INPUT_NAME, ''),
            'form_tag_input_value': get_params.get(settings.FORM_TAG_INPUT_NAME, ''),
            'form_observations_input_value': get_params.get(settings.FORM_OBSERVATIONS_INPUT_NAME, ''),
        }

    def get_context(self):
        context = self._get_base_context()
        form_params, google_params = EditLastEntryService.get_params()
        context.update(self._get_form_values_context())

        context.update({
            'title': 'Envelope',
            'edit_last_entry_form_params': form_params,
            'edit_last_entry_google_params': google_params
        })

        return context

    def POST(self):
        post_data = web.data()
        response = self._get_post_response(post_data)
        html_response = response.read()

        EditLastEntryService.set_params(
            form_params=post_data,
            google_params=ConfirmationPageParser.get_edit_last_response_form_params(html_response)
        )

        json_response = {
            'is_entry_recorded': ConfirmationPageParser.is_entry_recorded_for(html_response),
        }

        web.header('Content-Type', 'application/json')
        return json.dumps(json_response)

    def _get_post_response(self, poast_data):
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html'
        }

        action_url = settings.FORM_ACTION_URL
        params_dict = urlparse.parse_qs(poast_data)

        edit_last_entry_params = params_dict.get('edit-last-entry-params', '')

        if edit_last_entry_params:
            action_url += edit_last_entry_params

        conn = httplib.HTTPSConnection(settings.GOOGLE_DOCS_HOST)
        conn.request('POST', action_url, poast_data, headers)

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
