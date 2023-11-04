import datetime as dt
import smtplib
from random import choice
import os

SEND_DAY = 6
MY_EMAIL = "robert.d.python@gmail.com"
GMPSW = os.environ['GMPSW']
RECIPIENT = "robertdpython@yahoo.com"


now = dt.datetime.now()
today = now.isoweekday()

if SEND_DAY == today:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        today_quote = choice(all_quotes)
        # print(today_quote)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=GMPSW)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECIPIENT,
                msg=f"Subject:Motivational Quote\n\n{today_quote}"
            )
