import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

def send_email_alert(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(message)
    print(f"Email sent to {to_email} with subject '{subject}'")

def send_sms_alert(body, to_phone, from_phone, twilio_sid, twilio_auth_token):
    client = Client(twilio_sid, twilio_auth_token)
    message = client.messages.create(
        body=body,
        from_=from_phone,
        to=to_phone
    )
    print(f"SMS sent to {to_phone} with body '{body}'")

def send_alert(alert_message):
    subject = "Security Alert"
    from_email = "your-email@example.com"
    to_email = "recipient-email@example.com"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    smtp_user = "your-email@example.com"
    smtp_password = "your-email-password"

    to_phone = "+1234567890"
    from_phone = "+0987654321"
    twilio_sid = "your_twilio_sid"
    twilio_auth_token = "your_twilio_auth_token"

    send_email_alert(subject, alert_message, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password)
    send_sms_alert(alert_message, to_phone, from_phone, twilio_sid, twilio_auth_token)
