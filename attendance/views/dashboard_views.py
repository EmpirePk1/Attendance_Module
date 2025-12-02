# views/dashboard_views.py

from django.shortcuts import render, redirect

def dashboard_view(request):
    user_id = request.session.get("user_id")
    role = request.session.get("role")
    user_name = request.session.get("user_name", "")

    # If not logged in, redirect to login
    if not user_id or not role:
        return redirect("/login/")

    # Render dashboard with role-specific buttons
    return render(request, "dashboard.html", {
        "user_name": user_name,
        "role": role
    })

def logout_view(request):
    request.session.flush()  # Clear all session data
    return redirect("/login/")
