import imaplib, smtplib
from database import get_response_from_googlesheet_data
import time
import get_emails


class reply_to_text(object):
    def __init__(self):
        self.M = imaplib.IMAP4_SSL('imap.gmail.com')
        self.time_between_checks = 5
        self.sleep_adjustment = 0.25

    def send_reply_to_text(self, single_response_from_dictionary, username, password, google_sheet_info):
        global date_last_reply
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(username, password)
        print single_response_from_dictionary

        msg = "\r\n".join([
          "From: " + username,
          "To: " + single_response_from_dictionary['Reply Address'],
          "Subject: Text Reply",
          "",
          "" + get_response_from_googlesheet_data(single_response_from_dictionary['Key Phrase'], google_sheet_info)
          ])

        print msg
        smtp_server.sendmail(username, single_response_from_dictionary['Reply Address'], msg)
        smtp_server.quit()
        get_emails.date_last_reply = single_response_from_dictionary['Date']

    def reply_to_multiple_texts(self, username, password, mailbox, google_sheet_info):
        if mailbox[1] > 0:
            for reply in xrange(mailbox[1]):
                self.send_reply_to_text(mailbox[0][mailbox[1] - reply - 1], username, password, google_sheet_info)
                time.sleep(self.sleep_adjustment)
