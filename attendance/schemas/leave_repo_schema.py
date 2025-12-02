import datetime
from bson import ObjectId

def LeaveReportSchema(staff_id: str, leave_date: str, leave_message: str, leave_status: str):
    return {
        "staff_id": ObjectId(staff_id),
        "leave_date": leave_date,
        "leave_message": leave_message,
        "leave_status": leave_status,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
