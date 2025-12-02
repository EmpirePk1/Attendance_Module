import datetime
from bson import ObjectId

def NotificationSchema(staff_id: str, message: str):
    return {
        "staff_id": ObjectId(staff_id),
        "message": message,
        "read": False,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
