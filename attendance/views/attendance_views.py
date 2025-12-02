from django.shortcuts import render, redirect
from ..services.attendance_service import (
    make_attendance, update_attendance, delete_attendance,
    list_all_attendance_reports, list_reports_for_staff, staff_checkin_checkout
)
from ..utils.decorators import role_required

# ---------------- Admin: Attendance ----------------
@role_required("admin")
def list_attendance_view(request):
    records = list_all_attendance_reports()
    return render(request, "attendance/list.html", {"records": records, "role": "admin"})

@role_required("admin")
def update_attendance_view(request, attendance_id):
    update_attendance(attendance_id)
    return redirect("/attendance/list/")

@role_required("admin")
def delete_attendance_view(request, attendance_id):
    delete_attendance(attendance_id)
    return redirect("/attendance/list/")

# ---------------- Staff: My Attendance ----------------
@role_required("staff")
def list_my_attendance_view(request):
    staff_id = request.session.get("user_id")
    records = list_reports_for_staff(staff_id)
    return render(request, "attendance/list.html", {"records": records, "role": "staff"})

# ---------------- Staff: Check-in/Check-out ----------------
@role_required("staff")
def staff_checkin_checkout_view(request):
    staff_id = request.session.get("user_id")
    if request.method == "POST":
        action = request.POST.get("action")
        staff_checkin_checkout(staff_id, action)
        return redirect("/dashboard/")
    return render(request, "attendance/checkin_checkout.html")
