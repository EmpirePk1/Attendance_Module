import os
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI")

if not MONGO_URI:
    # Prevent crash during build on Railway
    print("Warning: MONGO_URI is not set — build environment")
    MONGO_URI = "mongodb://0.0.0.0"  # dummy fallback

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

