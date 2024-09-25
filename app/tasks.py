from app import celery
from celery.schedules import crontab

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Sends a daily reminder at 6 PM every day
    sender.add_periodic_task(
        crontab(hour=18, minute=0),
        send_daily_reminders.s(),
    )

@celery.task
def send_daily_reminders():
    # logic to send reminders
    pass
