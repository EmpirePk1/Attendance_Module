import datetime

def DepartmentSchema(name: str):
    return {
        "name": name,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
