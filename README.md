# 📧 Automated Invoice Email Reminder

This project automatically sends email reminders to clients about upcoming or overdue invoice payments, based on data from a Google Sheet.

## 🚀 Features

- Scheduled email reminders using **GitHub Actions**
- Google Sheet as a dynamic data source
- Emails sent via **Gmail SMTP**
- Sensitive data managed using environment variables
- Built with **Python** and **pandas**


<table>
  <tr>
    <td>

## 🔄 How It Works (Flow)<br><br>
1. GitHub Action triggers daily at 6 AM UTC.
2. Reads Google Sheet from public CSV export link.
3. Parses dates and filters unpaid reminders due today.
4. Sends personalized emails via Gmail SMTP.

    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/e1fc549c-cac3-4bc5-99d8-d95f1c09dabd" width="400" height="400" />
    </td>
  </tr>
</table>



## 🛠️ Setup Instructions
### 1. Clone this repo
```
git clone https://github.com/ShrutiGupta37/Email-Automation.git
```
### 2. Create and Fill .env File
```
EMAIL = Your Email id
PASSWORD = Email id Password 
URL = Google sheet URL
```
### 3. Install required libraries
```
pip install -r requirements.txt
```
### 4. Test the Script Locally
```
python main.py
```
If setup is correct, emails will be sent and you'll see:<br>
Total Emails Sent: X

### 5. Set Up GitHub Secrets
On GitHub: <br>

`Go to your repo → Settings → Secrets and Variables → Actions`

Add the following secrets:

`EMAIL`,`PASSWORD`,`URL`(the CSV export link of your Google Sheet)

### 6. Enable GitHub Actions
Ensure this file exists in your repo:
`.github/workflows/email-cron.yml`

Then push your code and GitHub Actions will take care of sending emails daily at the specified time!
```
git add .
git commit -m "Initial automation setup"
git push
```
You can also manually trigger the workflow from the Actions tab on GitHub.





