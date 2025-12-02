import datetime

def AdminSchema(name: str, email: str, password: str):
    return {
        "name": name,
        "email": email,
        "password": password,
        "created_at": datetime.datetime.utcnow(),
        "updated_at": datetime.datetime.utcnow()
    }
