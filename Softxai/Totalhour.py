import sys
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from dcg_service.core.exceptions import APIException
from dcg_service.core.response import custom_response
from flask_sqlalchemy import SQLAlchemy
from settings import db
import schedule
import time

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

# Add project path to system path
current_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(current_path, "..", ".."))
sys.path.append(project_path)

# Import models
from models import Event, EventPeriod, Period


def create_cron_jobs_for_events():
    events = Event.query.all()
    for event in events:
        event_periods = EventPeriod.query.filter_by(event_id=event.id).all()
        for event_period in event_periods:
            period = Period.query.get(event_period.period_id)
            if period:
                create_cron_job(event.name, period.period_value)


def create_cron_job(event_name, period_value):
    if period_value == 60.00:
        schedule_jobs(period_value)
    elif period_value == 1440.00:
        # schedule.every(period_value).minutes.do(hourly_event_data)
        schedule_jobs(period_value)
    elif period_value == 10080.00:
        schedule_jobs(period_value)
    elif period_value == 20160.00:
        schedule_jobs(period_value)
    elif period_value == 43200.00:
        schedule_jobs(period_value)
    elif period_value == 129600.00:
        schedule_jobs(period_value)
    elif period_value == 259200.00:
        schedule_jobs(period_value)
    elif period_value == 518400.00:
        schedule_jobs(period_value)
    elif period_value == 1036800.00:
        schedule_jobs(period_value)
    elif period_value == 1555200.00:
        schedule_jobs(period_value)
    elif period_value == -1.00:
        schedule_jobs(period_value)
    else:
        print(f"Unsupported period value: {period_value}")

def hourly_event_data():
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=1)
    return get_login_activity_data(start_time, end_time)

def weekly_event_data():
    end_time = datetime.now()
    start_time = end_time - timedelta(weeks=1)
    return get_login_activity_data(start_time, end_time)

def monthly_event_data():
    end_time = datetime.now()
    start_time = end_time - timedelta(days=30)
    return get_login_activity_data(start_time, end_time)

def get_login_activity_data(start_time, end_time):
    login_activity_data = UserLoginActivity.query.filter(
        UserLoginActivity.login_datetime >= start_time,
        UserLoginActivity.login_datetime <= end_time
    ).all()

    return login_activity_data

def schedule_jobs(period_value):
    if period_value == -1:
        schedule.every().day.at("00:00").do(hourly_event_data)
    else:
        schedule.every(period_value).minutes.do(hourly_event_data)

if __name__ == "__main__":
    create_cron_jobs_for_events()
    while True:
        schedule.run_pending()
        time.sleep(1)