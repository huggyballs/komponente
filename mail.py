import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "upravljanjepristupom@gmail.com"
receiver_email = "mraic00@fesb.hr"
password = "emovis123"
message = """\
Subject: Hi there

This message is sent from Python."""
message2 = """\
Subject: Hi there

This message is sent from Python.2"""

def sendEmail(msg):
    server = smtplib.SMTP('smtp.gmail.com', port)
    try:
        server = smtplib.SMTP('smtp.gmail.com', port)
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        if msg == 1
            server.sendmail(sender_email, receiver_email, message)
        else:
            server.sendmail(sender_email, receiver_email, message2)
    except Exception as e:
        print(e)
    finally:
        server.quit()

odabir = input("Odaberite koju poruku slati, 1 ili 2?")
sendEmail(odabir)