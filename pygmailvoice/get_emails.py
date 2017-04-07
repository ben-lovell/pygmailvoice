import imaplib, email
import time, datetime
from oauth2client.service_account import ServiceAccountCredentials

date_current_run = datetime.datetime.utcnow()
date_last_reply = datetime.datetime.utcnow()


class get_mail(object):
    def __init__(self):
        self.M = imaplib.IMAP4_SSL('imap.gmail.com')
        self.texts_to_reply_dict = {}
        self.emails_to_consider = 10
        self.mailbox = ''
        self.time_between_checks = 5
        self.sleep_adjustment = 0.25

    def find_between(self, s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""

    def login_and_check_mailbox(self, username, password, mailbox):
        time.sleep(self.time_between_checks)
        try:
            self.M.login(username, password)
        except imaplib.IMAP4.error:
            print "LOGIN FAILED!!! "
            # ... exit or deal with failure...
        rv, data = self.M.select(mailbox)
        if rv == 'OK':
            self.mailbox = self.process_mailbox()
            self.M.close()
            return self.mailbox

    def get_message_from_email(self, num_emails, for_loop_num):
        rv, data = self.M.fetch(str(num_emails - int(for_loop_num)), '(RFC822)')
        if rv != 'OK':
            print "ERROR getting message", for_loop_num

        msg = email.message_from_string(data[0][1])

        return msg

    def clean_email_date(self, msg):
        date_cleaning = msg['Date'][5:len(msg['Date'])-6]
        email_date_clean = datetime.datetime.strptime(date_cleaning, '%d %b %Y %H:%M:%S')

        return email_date_clean

    def get_data_from_good_text(self, msg, email_date_clean, num, data):
        reply_address = ""
        key_phrase = ""
        reply_address = msg['From'][18:-1]

        # find key phrase in msg
        key_phrase = self.find_between(str(msg)[3000:5000], "<https://www.google.com/voice/>", "YOUR ACCOUNT")

        # find and clean return address
        reply_address = ""
        if "@txt.voice.google.com" in msg['From']:
            reply_address = msg['From'][18:-1]

        self.texts_to_reply_dict[num] = {'Reply Address':reply_address, 'Key Phrase':key_phrase.strip(), 'Date':email_date_clean}
        print self.texts_to_reply_dict[num]

    def process_mailbox(self):
        rv, data = self.M.search(None, "ALL")
        if rv != 'OK':
            print "No messages found!"

        print "_______________________________"
        print "The current time is: " + str(datetime.datetime.utcnow())
        print "_______________________________"

        num_emails = len(data[0].split())

        for num in xrange(self.emails_to_consider):

            if self.emails_to_consider - int(num) != 0:
                msg = self.get_message_from_email(num_emails, num)

                if "@txt.voice.google.com" in msg['From']:
                    clean_email_date = self.clean_email_date(msg)

                    print "****"
                    print "-email date: " + str(clean_email_date)
                    print "-last run time: " + str(date_last_reply)

                    if clean_email_date > date_last_reply:
                        print "-Text will be sent: True"
                        self.get_data_from_good_text(msg, clean_email_date, num, data)

                else:
                    print "-Text will be sent: False"
                    continue

        return self.texts_to_reply_dict, len(self.texts_to_reply_dict)
