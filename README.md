# pygmailvoice

Pygooglevoice stopped working for me a few months back, so I built this quick substitute that uses gmail to see and respond to messages on Google Voice.

When setting this up, it is necessary to have your Google Voice account forward all incoming messages to a gmail account (look for this under the Google Voice account settings). In this gmail account, go under settings and allow IMAP (https://support.google.com/mail/answer/7126229?hl=en), and potentially less secure apps (https://support.google.com/accounts/answer/6010255?hl=en)

If you are looking to send automated responses, the code currently looks to find these responses on a google spreadsheet, you can find the doc for the gpsread library used here (https://gspread.readthedocs.io/en/latest/). The responses are found on the google sheet by first looking up the unique identifier code sent in the text, and returning the value from the indicated response column on google sheets.

Everything else should hopefully be explained in run_gmail_autotext.py. I'll be updating this as I go so let me know if you have any requests or questions.
