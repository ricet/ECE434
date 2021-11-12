#!/usr/bin/env python3

from __future__ import print_function
import time, math, os, sys, pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SPREADSHEET_ID = '1lRBoDwy2f_RQIS3q_zubzs_EQBxOlWuSxRg0qVEB7Uc'

def read_temp(sensor_num):
    if os.path.isdir("/sys/class/hwmon/hwmon" + str(sensor_num)):
        with open("/sys/class/hwmon/hwmon" + str(sensor_num) + "/temp1_input") as f:
            return int(f.read())/1000
    else:
        print("Invalid sensor number")
        return None

def main():
    
    # Exit if no sensors are found
    if not os.path.isdir("/sys/class/hwmon/hwmon0"):
        sys.exit("No temp sensors found!")
    
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            # creds = flow.run_local_server(port=0)
            creds = flow.run_console()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    sample_num = 1

    while (1):
        values = [ [time.time()/60/60/24+ 25569 - 4/24, read_temp(0), read_temp(1), read_temp(2)]]
        body = {'values': values}
        row = 'A' + str(sample_num)
        result = sheet.values().append(spreadsheetId=SPREADSHEET_ID,
                            range=row,
                            valueInputOption='USER_ENTERED', 
                            body=body
                            ).execute()
        sample_num = sample_num + 1
        time.sleep(5)


if __name__ == "__main__":
    main()