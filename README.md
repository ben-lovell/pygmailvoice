# pygmailvoice

Pygooglevoice stopped working for me a few months back, so I built this quick and dirty substitute that uses gmail to see and respond to messages on Google Voice.

When setting this up, it is necessary to have your Google Voice account forward all incoming messages to a gmail account (look for this under the Google Voice account settings). In this gmail account, go under settings and allow IMAP (https://support.google.com/mail/answer/7126229?hl=en)

If you are looking to send automated responses, the code currently looks to find these responses on a google spreadsheet, you can find the doc for the language here (https://gspread.readthedocs.io/en/latest/)

Everything else should hopefully be explained in run_gmail_autotext.py. I'll be updating this as I go so let me know if you have any requests.
