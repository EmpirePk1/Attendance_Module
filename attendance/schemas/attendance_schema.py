import datetime
from bson import ObjectId

def AttendanceSchema(department_id: str, attendance_date: str):
    return {
        "department_id": ObjectId(department_id),
        "attendance_date": attendance_date,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
