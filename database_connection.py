import os
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI")  # safer way
if not MONGO_URI:
    raise Exception("MONGO_URI environment variable is not set!")

client = MongoClient(MONGO_URI)
db = client["hrmsxdb"]

admin_col = db["admin"]
departments_col = db["departments"]
staff_col = db["staff"]
leave_col = db["leave_report"]
attendance_col = db["attendance"]
attendance_report_col = db["attendance_report"]
notifications_col = db["notifications"]
feedback_col = db["feedback_staff"]

