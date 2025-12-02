from database_connection import leave_col
from bson import ObjectId
import datetime

# ---------------- Create Leave ----------------
def create_leave_report(staff_id, leave_date, leave_message, leave_status="Pending"):
    leave = {
        "staff_id": staff_id,
        "leave_date": leave_date,
        "leave_message": leave_message,
        "leave_status": leave_status,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
    return leave_col.insert_one(leave).inserted_id

# ---------------- Create Leave Request (Staff) ----------------
def apply_leave(staff_id, leave_date, leave_message):
    leave = {
        "staff_id": staff_id,
        "leave_date": leave_date,
        "leave_message": leave_message,
        "leave_status": "Pending",
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
    return leave_col.insert_one(leave).inserted_id

# ---------------- List Leaves ----------------
def list_all_leaves():
    leaves = list(leave_col.find())
    for leave in leaves:
        leave["id"] = str(leave["_id"])
    return leaves

def list_leaves_for_staff(staff_id):
    leaves = list(leave_col.find({"staff_id": staff_id}))
    for leave in leaves:
        leave["id"] = str(leave["_id"])
    return leaves

# ---------------- Get Single Leave ----------------
def get_leave(leave_id):
    leave = leave_col.find_one({"_id": ObjectId(leave_id)})
    if leave:
        leave["id"] = str(leave["_id"])
    return leave

# ---------------- Update Leave ----------------
def update_leave(leave_id, leave_status=None):
    update_fields = {"updated_at": datetime.datetime.utcnow()}
    if leave_status:
        update_fields["leave_status"] = leave_status
    leave_col.update_one({"_id": ObjectId(leave_id)}, {"$set": update_fields})

# ---------------- Update Leave Status (Admin specific) ----------------
def update_leave_status(leave_id, status):
    leave_col.update_one(
        {"_id": ObjectId(leave_id)},
        {"$set": {"leave_status": status, "updated_at": datetime.datetime.utcnow()}}
    )

# ---------------- Delete Leave ----------------
def delete_leave(leave_id):
    leave_col.delete_one({"_id": ObjectId(leave_id)})
