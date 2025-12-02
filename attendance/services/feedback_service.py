from database_connection import feedback_col
from bson import ObjectId
import datetime

# ---------------- Create Feedback (Staff only) ----------------
def create_feedback_report(staff_id, feedback_text, feedback_reply=""):
    feedback = {
        "staff_id": staff_id,
        "feedback": feedback_text,
        "feedback_reply": feedback_reply,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
    return feedback_col.insert_one(feedback).inserted_id

# ---------------- List Feedbacks ----------------
def list_feedbacks():
    """Admin: list all feedbacks"""
    feedbacks = list(feedback_col.find())
    for feedback in feedbacks:
        feedback["id"] = str(feedback["_id"])
    return feedbacks

def list_feedback_for_staff(staff_id):
    """Staff: list only their feedbacks"""
    feedbacks = list(feedback_col.find({"staff_id": staff_id}))
    for feedback in feedbacks:
        feedback["id"] = str(feedback["_id"])
    return feedbacks

# ---------------- Get Single Feedback ----------------
def get_feedback(feedback_id):
    feedback = feedback_col.find_one({"_id": ObjectId(feedback_id)})
    if feedback:
        feedback["id"] = str(feedback["_id"])
    return feedback

# ---------------- Update Feedback (Admin only) ----------------
def update_feedback(feedback_id, feedback_reply=None):
    update_fields = {"updated_at": datetime.datetime.utcnow()}
    if feedback_reply is not None:
        update_fields["feedback_reply"] = feedback_reply
    feedback_col.update_one({"_id": ObjectId(feedback_id)}, {"$set": update_fields})

# ---------------- Delete Feedback (Admin only) ----------------
def delete_feedback(feedback_id):
    feedback_col.delete_one({"_id": ObjectId(feedback_id)})
