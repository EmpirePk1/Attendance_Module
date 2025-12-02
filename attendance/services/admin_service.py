from database_connection import admin_col
from bson import ObjectId
import datetime

def create_admin(name, email, password):
    admin = {
        "name": name,
        "email": email,
        "password": password,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
    return admin_col.insert_one(admin).inserted_id

def get_admin_by_id(admin_id):
    admin = admin_col.find_one({"_id": ObjectId(admin_id)})
    if admin:
        admin["id"] = str(admin["_id"])
    return admin

def list_admins():
    admins = list(admin_col.find())
    for admin in admins:
        admin["id"] = str(admin["_id"])
    return admins

def update_admin(admin_id, name=None, email=None, password=None):
    update_fields = {"updated_at": datetime.datetime.utcnow()}
    if name:
        update_fields["name"] = name
    if email:
        update_fields["email"] = email
    if password:
        update_fields["password"] = password
    admin_col.update_one({"_id": ObjectId(admin_id)}, {"$set": update_fields})

def delete_admin(admin_id):
    admin_col.delete_one({"_id": ObjectId(admin_id)})
