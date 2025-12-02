from database_connection import departments_col
from bson import ObjectId
import datetime

def create_department(name):
    department = {
        "name": name,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
    return departments_col.insert_one(department).inserted_id

def get_department_by_id(department_id):
    department = departments_col.find_one({"_id": ObjectId(department_id)})
    if department:
        department["id"] = str(department["_id"])
    return department

def list_departments():
    departments = list(departments_col.find())
    for department in departments:
        department["id"] = str(department["_id"])
    return departments

def update_department(department_id, name=None):
    update_fields = {"updated_at": datetime.datetime.utcnow()}
    if name:
        update_fields["name"] = name
    departments_col.update_one({"_id": ObjectId(department_id)}, {"$set": update_fields})

def delete_department(department_id):
    departments_col.delete_one({"_id": ObjectId(department_id)})
