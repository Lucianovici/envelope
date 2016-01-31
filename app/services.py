# -*- coding: utf-8 -*-
"""
Services that help to manage Google Spreadsheet API
"""
import json

import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from os.path import join

import settings


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


class EditLastEntryService(object):
    """
    Service that helps to edit the last entry, by storing it locally in the filesystem.
    """

    filename = 'edit_last_entry_params'

    @classmethod
    def set_params(cls, form_params, google_params):
        path = cls._get_filename_path()
        f = open(path, 'w')
        f.writelines([form_params, google_params])
        f.close()

    @classmethod
    def get_params(cls):
        form_params = ''
        google_params = ''

        path = cls._get_filename_path()
        try:
            f = open(path, 'r')
            form_params = f.readline()
            google_params = f.readline()
            f.close()
        except IOError:
            pass

        return form_params, google_params

    @classmethod
    def _get_filename_path(cls):
        return join(settings.APP_ROOT_PATH, cls.filename)
