from datetime import date 
import pandas as pd  
from send_email import send_email  
from dotenv import load_dotenv


def load_df(url):
    parse_dates = ["Due_Date", "Reminder_date"]
    df = pd.read_csv(url, parse_dates=parse_dates, dayfirst=True)
    return df


def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row["Reminder_date"].date()) and (row["has_paid"] == "NO"):
            send_email(
                subject=f'[SHRUTI GUPTA] Invoice: {row["Invoice_no"]}',
                receiver_email=row["Email"],
                Name=row["Name"],
                Due_Date=row["Due_Date"].strftime("%d, %b %Y"),  
                Invoice_no=row["Invoice_no"],
                Amount=row["Amount"],
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"


if __name__ == "__main__":
    df = load_df(URL)
    print(query_data_and_send_emails(df))
