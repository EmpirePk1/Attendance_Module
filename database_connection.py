import os
import pymongo
from pymongo import MongoClient
from django.conf import settings

#MongoDB Atlas Connection
client = MongoClient(os.environ["MONGO_URI"])
db = client["hrmsxdb"]


# Creating Database Collections (Tables)
admin_col = db["admin"]
departments_col = db["departments"]
staff_col = db["staff"]
leave_col = db["leave_report"]
attendance_col = db["attendance"]
attendance_report_col = db["attendance_report"]
notifications_col = db["notifications"]
feedback_col = db["feedback_staff"]

