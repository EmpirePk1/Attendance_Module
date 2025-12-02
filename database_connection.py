import pymongo
from pymongo import MongoClient
from django.conf import settings

#MongoDB Atlas Connection
url =  "mongodb://localhost:27017/"
client = MongoClient(url)

# Selecting Database
db = client["HRMSXdb"]

# Creating Database Collections (Tables)
admin_col = db["admin"]
departments_col = db["departments"]
staff_col = db["staff"]
leave_col = db["leave_report"]
attendance_col = db["attendance"]
attendance_report_col = db["attendance_report"]
notifications_col = db["notifications"]
feedback_col = db["feedback_staff"]

