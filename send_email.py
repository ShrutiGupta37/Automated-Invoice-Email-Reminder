import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv  # pip install python-dotenv

PORT = 587  
EMAIL_SERVER = "smtp.gmail.com"

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")


def send_email(subject, receiver_email, Name,Due_Date, Invoice_no,Amount):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("SHRUTI GUPTA", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

  
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Hi {Name},</p>
        <p>I hope you are well.</p>
        <p>I just wanted to drop you a quick note to remind you that <strong>{Amount} INR</strong> in respect of our invoice {Invoice_no} is due for payment on <strong>{Due_Date}</strong>.</p>
        <p>I would be really grateful if you could confirm that everything is on track for payment.</p>
        <p>Best regards</p>
        <p>SHRUTI GUPTA</p>
      </body>
    </html>
    """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


