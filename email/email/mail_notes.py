import smtplib
from email.mime.text import MIMEText


def send_notes_email(email, notes):
    sender_email = "jokerdeva18@gmail.com"
    sender_password = "acnu bsol osui tlps"

    # Create the email message
    message = MIMEText(f"Your Notes : {notes}")
    message["Subject"] = "Sending Notes"
    message["From"] = sender_email
    message["To"] = email

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [email], message.as_string())
    return "done"


