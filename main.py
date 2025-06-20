from datetime import date 
import pandas as pd  
from send_email import send_email  



URL = f"https://docs.google.com/spreadsheets/d/1iaFJzx6orKnKWEe2UlQR3Y3Z0GEzsZ8SdriaYt2PKUI/edit?gid=0#gid=0"


def load_df(url):
    parse_dates = ["Due_Date", "Reminder_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df


def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row["Reminder_date"].date()) and (row["has_paid"] == "no"):
            send_email(
                subject=f'[SHRUTI GUPTA] Invoice: {row["Invoice_no."]}',
                receiver_email=row["Email"],
                name=row["Name"],
                due_date=row["Due_Date"].strftime("%d, %b %Y"),  
                invoice_no=row["Invoice_no."],
                amount=row["Amount"],
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"


if __name__ == "__main__":
    df = load_df(URL)
    query_data_and_send_emails(df)