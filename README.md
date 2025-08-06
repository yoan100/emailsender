# Email Sender (Made with python)

--

This is just a simple project i built during summer vacation.

## Features
- Sends emails from a **pre-configured default email account** (Gmail supported).
- Asks the user for:
  - Recipient email address.
  - Number of emails to send (1–100).
  - Path to an HTML file for the email content.
- Sends emails one by one via SMTP.

---

## Requirements
- Python 3

---

## Setup
1. **Download the script**

2. **Edit the script**:
   - Open `bulk_mailer.py` and set:
     ```python
     DEFAULT_EMAIL = "your_email@gmail.com"
     DEFAULT_PASSWORD = "your_app_password"
     SMTP_SERVER = "smtp.gmail.com"
     ```
   - Use an [App Password for Gmail](https://support.google.com/accounts/answer/185833).
     
---

## Usage
1. Prepare an HTML file:
   ```html
   <html>
     <body>
       <h1>Hello!</h1>
       <p>This is a test email.</p>
     </body>
   </html>
   ```

2. Run the script:
   ```bash
   python3 bulk_mailer.py
   ```

3. Enter:
   - Recipient email address
   - Number of emails (1–100)
   - Path to your HTML file

---

## Notes
- Do not use your main Gmail account. Create a dedicated account for sending.
- Gmail sending limit: ~500 emails/day for normal accounts.
- All emails will be sent to **one recipient**. For multiple recipients, the script needs an extension.
- The script is new, create an issue if you need help!

---
