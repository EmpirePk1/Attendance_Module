from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from database_connection import admin_col, staff_col

@csrf_exempt
def index_view(request):
    return render(request, "index.html")

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")
        user = None

        if role == "admin":
            user = admin_col.find_one({"email": email, "password": password})
        elif role == "staff":
            user = staff_col.find_one({"email": email, "password": password})

        if user:
            # Set session variables
            request.session["user_id"] = str(user["_id"])
            request.session["role"] = role
            request.session["user_name"] = user.get("name", "")
            return redirect("/dashboard/")  # Redirect to dashboard
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    # GET request
    return render(request, "login.html")

def dashboard_view(request):
    if "user_id" not in request.session:
        return redirect("/login/")

    user_name = request.session.get("user_name")
    role = request.session.get("role")

    return render(request, "dashboard.html", {
        "user_name": user_name,
        "role": role
    })



def logout_view(request):
    request.session.flush()
    return redirect("/login/")
