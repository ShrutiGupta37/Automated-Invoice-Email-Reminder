import smtplib
from email.message import EmailMessage
import ssl
import time

import pandas as pd
df = pd.read_csv('C:\Git Demo\Email-Automation\data.csv')

email_sender =' ' #add sender's email
email_password=' ' #add 16 digit password

subject= "Testing for Automatic email"
body = """
    This mail is sent for tesing purpose.
"""

def send_mail( ):
    for email in df['Email']:
        email_receiver = email
        em = EmailMessage()
        em['From']=email_sender
        em['To']=email_receiver
        em['subject']=subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())

        time.sleep(5)

send_mail()
print("All mails sent successfully")

