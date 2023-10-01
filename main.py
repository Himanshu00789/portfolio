import pandas
import datetime as dt
import smtplib
import random
username="himanshu09884@gmail.com"
password="anubobi@123"
##################### Hard Starting Project ######################


now = dt.datetime.now()
today_month=now.month
today_day=now.day

today_tuple=(today_month,today_day)



data= pandas.read_csv("birthdays.csv")
birthdays_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}


if today_tuple in birthdays_dict:
    birthday_person= birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        replaced_content=contents.replace("[NAME]",birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(username,password)
        connection.sendmail(from_addr=username,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{replaced_content}")


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



