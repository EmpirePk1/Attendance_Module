from django.shortcuts import render, redirect
from ..services.attendance_service import (
    list_all_attendance_reports, list_reports_for_staff,
    update_attendance_report, delete_attendance_report
)
from ..utils.decorators import role_required

# ---------------- Admin ----------------
@role_required("admin")
def list_attendance_reports_view(request):
    reports = list_all_attendance_reports()
    return render(request, "attendance_reports/list.html", {"reports": reports, "role": "admin"})

@role_required("admin")
def update_attendance_report_view(request, report_id):
    if request.method == "POST":
        status = request.POST.get("status")
        update_attendance_report(report_id, status)
    return redirect("/attendance_reports/list/")

@role_required("admin")
def delete_attendance_report_view(request, report_id):
    delete_attendance_report(report_id)
    return redirect("/attendance_reports/list/")

# ---------------- Staff ----------------
@role_required("staff")
def list_my_attendance_reports_view(request):
    staff_id = request.session.get("user_id")
    reports = list_reports_for_staff(staff_id)
    return render(request, "attendance_reports/list.html", {"reports": reports, "role": "staff"})
