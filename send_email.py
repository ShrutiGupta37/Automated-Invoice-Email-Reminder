import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
import mimetypes
import ssl
import time
import pandas as pd

sender_email ='finalyearprojectemail419@gmail.com' #add sender's email
email_password='uiic ukco mpfi zrdx'       #add 16 digit password
df = pd.read_csv('C:\Git Demo\Email-Automation\data.csv')
df['Email'] = df['Email'].astype(str).str.strip()   

subject= "Testing for Automatic email"
attach_file= True

if attach_file:
    file_paths = [r'C:\Git Demo\Email-Automation\data.csv',r'C:\Git Demo\Git-Practice\git-cheat-sheet-education.pdf']  #add file paths which you want to send
    file_name = "data.csv"


def send_email(subject, receiver_email, name, phone_no):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.add_alternative(
        f"""\
        <html>
          <body>
            <p>Hi {name},</p>
            <p>I hope you are well.</p>
            <p>This is just a quick note to confirm that your registered phone number is: <strong>{phone_no}</strong>.</p>
            <p>If this is incorrect, please update us soon.</p>
            <p>Best regards,<br><strong>Shruti Gupta</strong></p>
          </body>
        </html>
        """,
        subtype="html",
    )


    if attach_file:
        for file_path in file_paths:
            if os.path.isfile(file_path):
                with open(file_path, "rb") as f:
                    file_data = f.read()
                    mime_type, _ = mimetypes.guess_type(file_path)
                    maintype, subtype = mime_type.split("/") if mime_type else ("application", "octet-stream")
                    msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=os.path.basename(file_path))


    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls(context=context)
        server.login(sender_email, email_password)
        server.send_message(msg)


if __name__ == "__main__":
    for index, row in df.iterrows():
        try:
            send_email(
                subject=subject,
                name=row["Name"],
                receiver_email=row["Email"],
                phone_no=row["Phone no."]
            )
            print(f"Sent to {row['Email']}")
            time.sleep(2)
        except Exception as e:
            print(f"Failed for {row['Email']}: {e}")

    print("\nAll emails are sent!")
