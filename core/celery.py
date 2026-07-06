from celery import Celery
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from core.config import BROKER, EMAIL_PASS, SENDER_EMAIL

# print(EMAIL_PASS)
# print(SENDER_EMAIL)

celery_app = Celery(
    "tasks",
    broker=BROKER
)

def func_send_email(receiver_email,html_text,message):
    smtp_server = "smtp.gmail.com"
    password = EMAIL_PASS
    sender_email = SENDER_EMAIL
    receiver_email = receiver_email

    message.attach(html_text)
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server,465,context=context) as server:
            server.login(sender_email,password)
            server.sendmail(sender_email,receiver_email,message.as_string())
            print("mail send")
    except Exception as e:
        print(e)

def func_registration_email(receiver_email):
    html = """
        <html>
            <body>
            <p><b>Registration successfull</b></p>
            </body>
        </html>
    """

    html_text = MIMEText(html,"html")

    message = MIMEMultipart("alternative")
    message['Subject'] = "Registration successfull"
    message['From'] = sender_email
    message['To'] = receiver_email
    return func_send_email(receiver_email,html_text,message)

def func_transaction_email(receiver_email,type,amount):
    html = f"""
        <html>
            <body>
            <p><b>Transaction succesfull</b></p>
            <p>{amount} {type} from your account<b>
            </body>
        </html>
    """

    html_text = MIMEText(html,"html")

    message = MIMEMultipart("alternative")
    message['Subject'] = "Transaction successfull"
    message['From'] = sender_email
    message['To'] = receiver_email
    return func_send_email(receiver_email,html_text,message)


@celery_app.task
def send_registration_email(email_id):   
    receiver_email = email_id
    return func_registration_email(receiver_email)

@celery_app.task
def send_transaction_email(email_id,type,amount):
    receiver_email = email_id
    return func_transaction_email(receiver_email,type,amount)