import os
import smtplib
from email.message import EmailMessage
import mimetypes
import ssl
import time
import pandas as pd

email_sender =' '           #add sender's email
email_password=' '           #add 16 digit password
df = pd.read_csv('C:\Git Demo\Email-Automation\data.csv')

email_sender =' ' #add sender's email add
email_password=' ' #add 16 digit password
email_receiver =' ' #add receiver's email add

subject= "Testing for Automatic email"
attach_file= True

if attach_file:
    file_paths = [r' ',r' ']  #add file paths which you want to send
    file_name = "data.csv"


def send_mail( ):
    for index,row in df.iterrows():
        name = row['Name']
        email_receiver = row['Email']

        body = f"""
hi {name},
This mail is sent for tesing purpose.
Thank you for your support.
Shruti Gupta

"""

        em = EmailMessage()
        em['From']=email_sender
        em['To']=email_receiver
        em['subject']=subject
        em.set_content(body)

        if attach_file:
            for file_path in file_paths:
                mime_type, _ = mimetypes.guess_type(file_path)
                if mime_type:
                    maintype, subtype = mime_type.split('/')
                else:
                    maintype, subtype = 'application', 'octet-stream'

                with open(file_path, 'rb') as f:
                    em.add_attachment(
                        f.read(),
                        maintype=maintype,
                        subtype=subtype,
                        filename=os.path.basename(file_path)
                    )

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())

        time.sleep(2)

send_mail()
print("All mails are sent successfully")

