from get_emails import get_mail
from respond import reply_to_text


username = "enterusername@gmail.com"
password = "enter_password"
inbox = "enter inbox to look at"

google_sheet_info = [
    "worksheet key",                                    #worksheet_key
    "sheet in worksheet",                               #sheet
    "column to pull repsonses from",                    #column_with_text
    "column with unique ID for response",               #column_num_with_unique_id_number
    "example google sheet json key.json"                #credential_json
    ]

while True:
    gt = get_mail()
    rtt = reply_to_text()
    mailbox = gt.login_and_check_mailbox(username, password, inbox)
    if mailbox[1] > 0:
        rtt.reply_to_multiple_texts(username, password, mailbox, google_sheet_info)
