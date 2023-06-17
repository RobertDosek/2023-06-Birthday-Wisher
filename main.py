import datetime as dt
import pandas as pd
import smtplib
from random import randint

MY_EMAIL = "robert.d.python@gmail.com"
GMPSW = "mgtszwmykzrvkzkk"

now = dt.datetime.now()
today = (now.month, now.day)

df = pd.read_csv("birthdays.csv")
df_dict = df.to_dict(orient="records")
# print(df_dict)

for e in df_dict:
    birthday = (e["month"], e["day"])
    if today == birthday:
        rec_name = e["name"]
        email = e["email"]
        with open(f"letter_templates/letter_{randint(1,3)}.txt") as letter:
            content = letter.read()
            new_content = content.replace("[NAME]", rec_name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=GMPSW)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy birthday!!\n\n{new_content}"
            )




