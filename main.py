##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random

# 1. Update the birthdays.csv
df = pandas.read_csv("D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-32/birthdays.csv")
date = df.to_dict(orient="records")



# 2. Check if today matches a birthday in the birthdays.csv
my_email = "shubhamb42069@gmail.com"
password = "pmif sdeb bkgi pzir"
letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

today = dt.datetime.now()
today_month = today.month
today_day = today.day

for i in date:
    if i["month"] == today_month and i["day"] == today_day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        txt = random.choice(letter_templates)
        file_path = f"D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-32/letter_templates/{txt}"
        with open(file_path, "r") as file:
            content = file.read()
            message = content.replace("[NAME]", i["name"])



# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(user=my_email, password=password)
            connect.sendmail(to_addrs=i["email"], from_addr=my_email, msg=f"Subject: Happy Birthday\n\n {message}")










