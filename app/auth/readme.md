Please follow the instructions from http://gspread.readthedocs.org/en/latest/oauth2.html

Although the instructions might be somehow outdated, you should be able to:

1. Create a new project.
2. Go to API Manager and select Credentials section.
3. Add new Service Account `credentials` as json file.
4. `Share` your spreadsheet with the `client_email` from the json file. Read only permission is enough.   

Make sure you set your environment variable `ENVELOPE_AUTH_JSON_FILE_PATH` as an absolute path to your this json file. 
