import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

def send_email():
    # 從 GitHub Secrets 中獲取 SendGrid API 密鑰
    sendgrid_api_key = os.getenv('FirstApiKey')

    if not sendgrid_api_key:
        print("SENDGRID_API_KEY is not set.")
        return

    sg = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key)

    from_email = Email("a253.tw@yahoo.com.tw")  # 你的發件人郵件地址
    to_email = To("a253.tw@yahoo.com.tw")  # 收件人郵件地址
    subject = "Test Email from GitHub Actions"
    content = Content("text/plain", "This is a test email sent from GitHub Actions.")

    mail = Mail(from_email, to_email, subject, content)

    try:
        response = sg.send(mail)
        print(f"Email sent successfully. Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    send_email()
