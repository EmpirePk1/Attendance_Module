import os
from pymongo import MongoClient, errors

# Get the MongoDB URI from environment variable
MONGO_URI = os.environ.get("MONGO_URI")

# Safety check: Ensure URI is set
if not MONGO_URI:
    raise ValueError(
        "MONGO_URI environment variable is not set! "
        "Go to Railway → Settings → Environment Variables and add it."
    )

# Safety check: Ensure URI starts with valid scheme
if not (MONGO_URI.startswith("mongodb://") or MONGO_URI.startswith("mongodb+srv://")):
    raise ValueError(
        "MONGO_URI is invalid! It must start with 'mongodb://' or 'mongodb+srv://'. "
        f"Current value: {MONGO_URI}"
    )

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    # Attempt a quick server check
    client.server_info()
except errors.ServerSelectionTimeoutError as err:
    raise ConnectionError(
        "Could not connect to MongoDB. Check your MONGO_URI and network settings."
    ) from err

# Database
db = client["hrmsxdb"]

# Collections
admin_col = db["admin"]
staff_col = db["staff"]
departments_col = db["departments"]
leave_col = db["leave_report"]
attendance_col = db["attendance"]
attendance_report_col = db["attendance_report"]
notifications_col = db["notifications"]
feedback_col = db["feedback_staff"]

print("✅ MongoDB connection successful!")
