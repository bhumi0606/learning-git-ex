from celery import Celery
from celery.schedules import crontab
from core.config import BROKER


# print(EMAIL_PASS)
# print(SENDER_EMAIL)

celery_app = Celery(
    "tasks",
    broker=BROKER,
    include=["tasks"]
)

celery_app.conf.beat_schedule = {
    "print-every-minute": {
        "task": "tasks.hello",
        "schedule": crontab(minute="*"),
    },
    "generate-daily-report":{
        "task": "tasks.daily_transaction_report",
        "schedule": crontab(hour=0,minute=0),
    },
}

