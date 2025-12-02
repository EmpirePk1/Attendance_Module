import datetime
from bson import ObjectId

def FeedbackSchema(staff_id: str, feedback: str, feedback_reply: str = None):
    return {
        "staff_id": ObjectId(staff_id),
        "feedback": feedback,
        "feedback_reply": feedback_reply,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
