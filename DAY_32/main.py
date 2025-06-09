# import smtplib
#
# my_email = "**********@gmail.com"
# my_password = "****************"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#
#     msg = "Subject:Hello\n\nThis is the body of my email."
#
#     connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=msg)
