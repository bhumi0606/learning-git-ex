from celery import Celery
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from core.config import BROKER, EMAIL_PASS

celery_app = Celery(
    "tasks",
    broker=BROKER
)

def func_email_send(sender_email,receiver_email,message):
    smtp_server = "smtp.gmail.com"
    password = EMAIL_PASS
    sender_email = sender_email
    receiver_email = receiver_email


    message = MIMEMultipart("alternative")
    message['Subject'] = "Registration successfull"
    message['From'] = sender_email
    message['To'] = receiver_email

    html = """
        <html>
            <body>
            <p><b>Registration successfull</b></p>
            </body>
        </html>
    """

    html_text = MIMEText(html,"html")

    message.attach(html_text)
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server,465,context=context) as server:
            server.login(sender_email,password)
            server.sendmail(sender_email,receiver_email,message.as_string())
            print("mail send")
    except Exception as e:
        print(e)
    
    
@celery_app.task
def send_email(email_id):   
    sender_email = "bhumikprajapati007@gmail.com"
    receiver_email = email_id
    return func_email_send(sender_email,receiver_email)
