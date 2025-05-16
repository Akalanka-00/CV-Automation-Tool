import smtplib
import os
from email.message import EmailMessage

from service.json_service import read_json_file


# Gmail SMTP server details

  # Use App Password if 2FA is enabled

def send_email(receiver_email, subject, body, cc=[]):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    config = read_json_file("configure.json")
    sender_email = config['email']
    app_password = config['password']

    msg = EmailMessage()
    # Create email message
    msg = EmailMessage()

    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg["Cc"] = ", ".join(cc)
    attachment_path = "./data/"+config['cv_name']
    if attachment_path != "":
        attachment_name = os.path.basename(attachment_path)

        try:
            with open(attachment_path, 'rb') as f:
                file_data = f.read()
                file_type = 'application/pdf'  # Change this if attaching a different file type
                msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=attachment_name)
        except FileNotFoundError:
            print(f"File {attachment_path} not found!")

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, app_password)
            server.send_message(msg)
            print("Successfully sent email to "+receiver_email)
    except Exception as e:
        print("Error:", e)
