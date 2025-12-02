import datetime
from bson import ObjectId

def StaffSchema(name: str, email: str, phone: str, password: str,
                department_id: str, gender: str, profile_pic: str = None):
    
    return {
        "name": name,
        "email": email,
        "phone": phone,
        "password": password,
        "department_id": ObjectId(department_id) if department_id else None,
        "gender": gender,
        "profile_pic": profile_pic,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
