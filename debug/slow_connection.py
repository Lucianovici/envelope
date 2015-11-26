# -*- coding: utf-8 -*-
"""
Debug a slow google API connection, measuring each step.
"""
import json
import time

import gspread
import pprint
from oauth2client.client import SignedJwtAssertionCredentials

start_time = time.time()
last_time_registered = time.time()


def print_tt(msg):
    global last_time_registered
    current_time = time.time()
    print("%r, %s | Spent %r" % (current_time, msg, current_time - last_time_registered))
    last_time_registered = current_time


def get_google_auth_json():
    auth_file = open('../app/auth/google_auth.json')
    print_tt("get_google_spreadsheet: Credentials file opened")
    auth_json = json.load(auth_file)
    auth_file.close()
    return auth_json


google_auth_json = get_google_auth_json()


def get_google_client():
    scope = ['https://spreadsheets.google.com/feeds']
    print_tt("get_google_spreadsheet: Json is available")
    credentials = SignedJwtAssertionCredentials(
        google_auth_json['client_email'], google_auth_json['private_key'].encode(), scope
    )
    print_tt("get_google_spreadsheet: SignedJwtAssertionCredentials available")
    gc = gspread.authorize(credentials)
    return gc


def get_google_spreadsheet():
    gc = get_google_client()
    print_tt("get_google_spreadsheet: Credentials passed")
    sheet = gc.open_by_key(google_auth_json['sheet_id'])
    print_tt("get_google_spreadsheet: Sheet opened by key")

    return sheet


google_spreadsheet = get_google_spreadsheet()

print_tt("Preparing to get the spreadsheet")
worksheet = google_spreadsheet.get_worksheet(0)
print_tt("We got the spreadsheet!")

worksheet_values = worksheet.get_all_values()

print_tt("We got the values for the worksheet")

print("Results:\n")
pprint.pprint(worksheet_values)

end_time = time.time()

print("TOTAL TIME SPENT %r" % (end_time - start_time))
