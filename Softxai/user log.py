import sys
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from dcg_service.core.exceptions import APIException
from dcg_service.core.response import custom_response
from flask_sqlalchemy import SQLAlchemy
from flask import request
from call_center.helper.models import UserLoginActivity
from settings import db

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)

current_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(current_path, "..", ".."))
sys.path.append(project_path)

def insert_login_activity_data():
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=1)

    login_activity_data = get_login_activity_data(start_time, end_time)

    insert_into_eventdata(login_activity_data)

def get_login_activity_data(start_time, end_time):
    login_activity_data = UserLoginActivity.query.filter(
        UserLoginActivity.login_datetime >= start_time,
        UserLoginActivity.login_datetime <= end_time
    ).all()

    return login_activity_data

def insert_into_eventdata(login_activity_data):
    for activity in login_activity_data:
        eventdata = {
            "user_id": activity.user_id,
            "login_datetime": activity.login_datetime,
            "logout_datetime": activity.logout_datetime,
        }
        # Example: db.session.execute("INSERT INTO eventdata (user_id, login_datetime, logout_datetime) VALUES (:user_id, :login_datetime, :logout_datetime)", eventdata)
        # Commit changes to the database
        db.session.commit()

if __name__ == "__main__":
    insert_login_activity_data()
