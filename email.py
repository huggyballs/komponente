import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "upravljanjepristupom@gmail.com"
receiver_email = "mraic00@fesb.hr"
password = input("Type your password and press enter:")
message = """\
Subject: Hi there

This message is sent from Python."""

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except:
    print('Error')
finally:
    server.quit()

