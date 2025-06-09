import datetime as dt
import random
import pandas
import smtplib

MY_EMAIL = "**********@gmail.com"
MY_PASSWORD = "****************"

##################### Normal Starting Project ######################
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_tuple = (now.month, now.day)

# HINT 2: Use pandas to read the birthdays.csv
df = pandas.read_csv("birthdays.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        email_message = f"Subject:Happy Birthday\n\n{contents}"
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthdays_person["email"], msg=email_message)



