from database_connection import staff_col
from bson import ObjectId
import datetime

def create_staff(name, email, phone, password, department_id, gender, profile_pic=None):
    staff = {
        "name": name,
        "email": email,
        "phone": phone,
        "password": password,
        "department_id": department_id,
        "gender": gender,
        "profile_pic": profile_pic,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
    return staff_col.insert_one(staff).inserted_id

def get_staff_by_id(staff_id):
    staff = staff_col.find_one({"_id": ObjectId(staff_id)})
    if staff:
        staff["id"] = str(staff["_id"])
    return staff

def list_staff():
    staff_list = list(staff_col.find())
    for staff in staff_list:
        staff["id"] = str(staff["_id"])
    return staff_list

def update_staff(staff_id, name=None, email=None, phone=None, gender=None):
    update_fields = {"updated_at": datetime.datetime.utcnow()}
    if name:
        update_fields["name"] = name
    if email:
        update_fields["email"] = email
    if phone:
        update_fields["phone"] = phone
    if gender:
        update_fields["gender"] = gender
    staff_col.update_one({"_id": ObjectId(staff_id)}, {"$set": update_fields})

def delete_staff(staff_id):
    staff_col.delete_one({"_id": ObjectId(staff_id)})
