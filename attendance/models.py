from django.db import models
from database_connection import db
import datetime

# Creating collection
admin_collection = db["admin"]

def create_admin_document(name, email, password):
    return {
        "name": name,
        "email": email,
        "password": password,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }