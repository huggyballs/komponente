import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "upravljanjepristupom@gmail.com"
receiver_email = "mraic00@fesb.hr"
password = "emovis123"
message = """\
Subject: Hi there

This message is sent from Python."""
server = smtplib.SMTP('smtp.gmail.com', port)
try:
    server = smtplib.SMTP('smtp.gmail.com', port)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print(e)
finally:
    server.quit()

