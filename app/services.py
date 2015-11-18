"""
Services that help to manage Google Spreadsheet API
"""
import json

import gspread
from oauth2client.client import SignedJwtAssertionCredentials


def get_google_auth_json():
    auth_file = open('auth/google_auth.json')
    print("get_google_spreadsheet: Credentials file opened")
    auth_json = json.load(auth_file)
    auth_file.close()
    return auth_json


google_auth_json = get_google_auth_json()


def get_google_client():
    scope = ['https://spreadsheets.google.com/feeds']
    print("get_google_spreadsheet: Json is available")
    credentials = SignedJwtAssertionCredentials(
        google_auth_json['client_email'], google_auth_json['private_key'].encode(), scope
    )
    print("get_google_spreadsheet: SignedJwtAssertionCredentials available")
    gc = gspread.authorize(credentials)
    return gc


def get_google_spreadsheet():
    gc = get_google_client()
    print("get_google_spreadsheet: Credentials passed")
    sheet = gc.open_by_key(google_auth_json['sheet_id'])
    print("get_google_spreadsheet: Sheet opened by key")

    return sheet


google_spreadsheet = get_google_spreadsheet()
