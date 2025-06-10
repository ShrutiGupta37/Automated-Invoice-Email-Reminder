import os
import smtplib
from email.message import EmailMessage
import ssl

email_sender =' ' #add sender's email add
email_password=' ' #add 16 digit password
email_receiver =' ' #add receiver's email add

subject= "Testing for Automatic email"
body = """
    This mail is sent for tesing purpose.
"""
em = EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())

