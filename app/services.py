# -*- coding: utf-8 -*-
"""
Services that help to manage Google Spreadsheet API
"""
import json

import gspread
from oauth2client.client import SignedJwtAssertionCredentials


class GoogleApiService(object):
    """
    Wrapper for google API and data access to spreadsheet.
    """
    auth_dict = {}

    def __init__(self, auth_json_file_path):
        self._set_auth_dict_from_file(auth_json_file_path)

    def _set_auth_dict_from_file(self, auth_json_file_path):
        auth_file = open(auth_json_file_path)
        self.auth_dict = json.load(auth_file)
        auth_file.close()

    def get_client(self):
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = SignedJwtAssertionCredentials(
            self.auth_dict['client_email'], self.auth_dict['private_key'].encode(), scope
        )
        client = gspread.authorize(credentials)
        return client

    def get_spreadsheet(self, sheet_id):
        client = self.get_client()
        return client.open_by_key(sheet_id)
