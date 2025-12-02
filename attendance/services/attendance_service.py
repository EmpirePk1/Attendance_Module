from database_connection import attendance_col, attendance_report_col
from bson import ObjectId
import datetime

# ---------------- Attendance ----------------
def make_attendance(department_id, attendance_date):
    attendance = {
        "department_id": ObjectId(department_id),
        "attendance_date": attendance_date,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
    return attendance_col.insert_one(attendance).inserted_id

def update_attendance(attendance_id):
    attendance_col.update_one(
        {"_id": ObjectId(attendance_id)},
        {"$set": {"updated_at": datetime.datetime.utcnow()}}
    )

def delete_attendance(attendance_id):
    attendance_col.delete_one({"_id": ObjectId(attendance_id)})

# ---------------- Attendance Reports ----------------
def create_attendance_report(staff_id, attendance_id, status):
    report = {
        "staff_id": staff_id,
        "attendance_id": attendance_id,
        "status": status,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
    return attendance_report_col.insert_one(report).inserted_id

def list_all_attendance_reports():
    reports = list(attendance_report_col.find())
    for report in reports:
        report["id"] = str(report["_id"])
    return reports

def list_reports_for_staff(staff_id):
    reports = list(attendance_report_col.find({"staff_id": staff_id}))
    for report in reports:
        report["id"] = str(report["_id"])
    return reports

def get_attendance_report(report_id):
    report = attendance_report_col.find_one({"_id": ObjectId(report_id)})
    if report:
        report["id"] = str(report["_id"])
    return report

def update_attendance_report(report_id, status):
    attendance_report_col.update_one(
        {"_id": ObjectId(report_id)},
        {"$set": {"status": status, "updated_at": datetime.datetime.utcnow()}}
    )

def delete_attendance_report(report_id):
    attendance_report_col.delete_one({"_id": ObjectId(report_id)})

# ---------------- Staff Check-in/Check-out ----------------
def staff_checkin_checkout(staff_id, action):
    today = datetime.datetime.utcnow()
    attendance = attendance_col.find_one({"attendance_date": today})
    if not attendance:
        attendance_id = make_attendance(department_id=None, attendance_date=today)
    else:
        attendance_id = str(attendance["_id"])

    existing_report = attendance_report_col.find_one({"staff_id": staff_id, "attendance_id": attendance_id})
    new_status = "Checked In" if action.lower() == "checkin" else "Checked Out"

    if not existing_report:
        create_attendance_report(staff_id, attendance_id, new_status)
    else:
        attendance_report_col.update_one(
            {"_id": existing_report["_id"]},
            {"$set": {"status": new_status, "updated_at": datetime.datetime.utcnow()}}
        )
