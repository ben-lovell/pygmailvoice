import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
from datetime import datetime

def get_response_from_googlesheet_data(idnum, google_sheet_info):

    partial_clean_idnum = [int(s) for s in str(idnum) if s.isdigit()]
    clean_idnum = ''
    for s in partial_clean_idnum:
        clean_idnum += str(s)

    worksheet_key = google_sheet_info[0]
    sheet = google_sheet_info[1]
    column_with_text = google_sheet_info[2]
    column_num_with_unique_id_number = google_sheet_info[3]

    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(google_sheet_info[4], scope)

    gc = gspread.authorize(credentials)

    # Open a worksheet from spreadsheet with one shot
    wks = gc.open_by_key(worksheet_key)
    worksheet = wks.worksheet(sheet)

    row_titles = worksheet.row_values(1)
    row = 0
    for i, j in enumerate(row_titles):
        if j == column_with_text:
            row = i + 1

    idnum_location = worksheet.col_values(column_num_with_unique_id_number)
    column = 0
    for i, j in enumerate(idnum_location):
        if j == clean_idnum:
            column = i + 1


    try:
        phrase = worksheet.cell(column, row).value
        if phrase != "":
            return phrase
        else:
            return "Please try texting the unique code again"
    except:
        return "Please try texting the unique code again"
