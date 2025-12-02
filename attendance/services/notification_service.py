from database_connection import notifications_col
from bson import ObjectId
import datetime

# ---------------- Create Notification (Admin only) ----------------
def create_notification(staff_id, message):
    notification = {
        "staff_id": staff_id,  # Can be specific staff or None for all
        "message": message,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
    return notifications_col.insert_one(notification).inserted_id

# ---------------- List Notifications (Admin sees all) ----------------
def list_notifications():
    notifications = list(notifications_col.find())
    for notification in notifications:
        notification["id"] = str(notification["_id"])
    return notifications

# ---------------- List Notifications (Staff sees only theirs) ----------------
def list_notifications_for_staff(staff_id):
    notifications = list(notifications_col.find({"staff_id": staff_id}))
    for notification in notifications:
        notification["id"] = str(notification["_id"])
    return notifications

# ---------------- Get Single Notification ----------------
def get_notification(notification_id):
    notification = notifications_col.find_one({"_id": ObjectId(notification_id)})
    if notification:
        notification["id"] = str(notification["_id"])
    return notification

# ---------------- Update Notification (Admin only) ----------------
def update_notification(notification_id, message=None, staff_id=None):
    update_fields = {"updated_at": datetime.datetime.utcnow()}
    if message is not None:
        update_fields["message"] = message
    if staff_id is not None:
        update_fields["staff_id"] = staff_id
    notifications_col.update_one({"_id": ObjectId(notification_id)}, {"$set": update_fields})

# ---------------- Delete Notification (Admin only) ----------------
def delete_notification(notification_id):
    notifications_col.delete_one({"_id": ObjectId(notification_id)})
