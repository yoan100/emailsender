import smtplib
import os
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ENTER SERVER CREDENTIALS | 
DEFAULT_EMAIL = "[EMAIL HERE]"
DEFAULT_PASSWORD = "[PW HERE]"  
SMTP_SERVER = "[SERVER HERE]"
SMTP_PORT = 587

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def main():
    print("=== Bulk Email Sender ===")
    print(f"Emails will be sent from: {DEFAULT_EMAIL}\n")

    recipient = input("Enter recipient email: ").strip()
    while not is_valid_email(recipient):
        recipient = input("Invalid email. Enter a valid recipient email: ").strip()

    while True:
        try:
            count = int(input("How many emails to send? (1-100): "))
            if 1 <= count <= 100:
                break
            else:
                print("Number must be between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    html_path = input("Enter the path to your HTML file: ").strip()
    while not os.path.isfile(html_path):
        html_path = input("File not found. Enter a valid path: ").strip()

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(DEFAULT_EMAIL, DEFAULT_PASSWORD)

        print("\nStarting to send emails...\n")

        for i in range(count):
            msg = MIMEMultipart("alternative")
            msg["Subject"] = f"Email #{i+1}"
            msg["From"] = DEFAULT_EMAIL
            msg["To"] = recipient

            msg.attach(MIMEText(html_content, "html"))

            server.sendmail(DEFAULT_EMAIL, recipient, msg.as_string())
            print(f"Email {i+1}/{count} sent successfully.")

        server.quit()
        print("\nAll emails sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
