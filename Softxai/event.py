import sys
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from dcg_service.core.exceptions import APIException
from dcg_service.core.response import custom_response
from flask_sqlalchemy import SQLAlchemy
from call_center.helper.models import UserLoginActivity, CallLog, OrderCommission
from settings import db

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

current_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(current_path, "..", ".."))
sys.path.append(project_path)

def hourly_event_data():
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=1)
    login_activity_data = get_login_activity_data(start_time, end_time)

def weekly_event_data():
    end_time = datetime.now()
    start_time = end_time - timedelta(weeks=1)
    login_activity_data = get_login_activity_data(start_time, end_time)
def monthly_event_data():
    end_time = datetime.now()
    start_time = end_time - timedelta(days=30)
    # process_event_data(start_time, end_time, "monthly")
    login_activity_data = get_login_activity_data(start_time, end_time)
# def process_event_data(start_time, end_time, interval):
#     if interval == "hourly":
#         login_activity_data = get_login_activity_data(start_time, end_time)
#     elif interval == "weekly":
#         login_activity_data = get_login_activity_data(start_time, end_time)
#     elif interval == "monthly":
#         login_activity_data = get_login_activity_data(start_time, end_time)
#     else:
#         print("Unsupported interval")
#         return
#     insert_event_data()

def get_login_activity_data(start_time, end_time):
    login_activity_data = UserLoginActivity.query.filter(
        UserLoginActivity.login_datetime >= start_time,
        UserLoginActivity.login_datetime <= end_time
    ).all()

    return login_activity_data

def insert_event_data(event_id, period_id, application_id, org_id, induavail_id, emp_id, user_id, user_group_id, service_id):
    event_data = EventData(
        event_id=event_id,
        period_id=period_id,
        application_id=application_id,
        org_id=org_id,
        induavail_id=induavail_id,
        emp_id=emp_id,
        user_id=user_id,
        user_group_id=user_group_id,
        service_id=service_id
    )

    db.session.add(event_data)
    db.session.commit()

if __name__ == "__main__":
    hour_data = hourly_event_data()
    if hour_data:
        insert_event_data("Total Hours","Hourly",)
    weekly_event_data()
    monthly_event_data()


import sys
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from dcg_service.core.exceptions import APIException
from dcg_service.core.response import custom_response
from flask_sqlalchemy import SQLAlchemy
from call_center.helper.models import UserLoginActivity, CallLog, OrderCommission
from settings import db

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

# Add project path to system path
current_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(current_path, "..", ".."))
sys.path.append(project_path)

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

def insert_event_data(event_id, period_id, application_id, org_id, induavail_id, emp_id, user_id, user_group_id, service_id):
    event_data = EventData(
        event_id=event_id,
        period_id=period_id,
        application_id=application_id,
        org_id=org_id,
        induavail_id=induavail_id,
        emp_id=emp_id,
        user_id=user_id,
        user_group_id=user_group_id,
        service_id=service_id
    )

    db.session.add(event_data)
    db.session.commit()

if __name__ == "__main__":
    hourly_data = hourly_event_data()
    if hourly_data:
        for data in hourly_data:
            insert_event_data(data.event_id, data.period_id, data.application_id, data.org_id, data.induavail_id, data.emp_id, data.user_id, data.user_group_id, data.service_id)
    weekly_data = weekly_event_data()
    if weekly_data:
        for data in weekly_data:
            insert_event_data(data.event_id, data.period_id, data.application_id, data.org_id, data.induavail_id, data.emp_id, data.user_id, data.user_group_id, data.service_id)
    monthly_data = monthly_event_data()
    if monthly_data:
        for data in monthly_data:
            insert_event_data(data.event_id, data.period_id, data.application_id, data.org_id, data.induavail_id, data.emp_id, data.user_id, data.user_group_id, data.service_id)
