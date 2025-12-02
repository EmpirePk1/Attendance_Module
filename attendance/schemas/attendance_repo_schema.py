import datetime
from bson import ObjectId

def AttendanceReportSchema(staff_id: str, attendance_id: str, status: str):
    return {
        "staff_id": ObjectId(staff_id),
        "attendance_id": ObjectId(attendance_id),
        "status": status,
        "check_in": None,
        "check_out": None,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
