from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from attendance.services.leave_service import (
    apply_leave,
    list_all_leaves,
    list_leaves_for_staff,
    get_leave,
    update_leave_status,
    delete_leave
)
from attendance.utils.decorators import role_required

# ---------------- List Leaves ----------------

@role_required("admin")
def list_leave_view(request):
    """
    Admin: View all leave requests
    """
    leaves = list_all_leaves()
    return render(request, "leave/list.html", {"leaves": leaves, "role": "admin"})

@role_required("staff")
def list_my_leave_view(request):
    """
    Staff: View only their own leaves
    """
    staff_id = request.session.get("user_id")
    leaves = list_leaves_for_staff(staff_id)
    return render(request, "leave/list.html", {"leaves": leaves, "role": "staff"})

@role_required("staff")
def apply_leave_view(request):
    if request.method == "POST":
        staff_id = request.session.get("user_id")  # Logged in staff
        leave_date = request.POST.get("leave_date")
        leave_message = request.POST.get("leave_message")

        apply_leave(staff_id, leave_date, leave_message)

        return redirect("/leave/mylist/")

    return render(request, "leave/apply.html")

# ---------------- Update Leave Status (Admin only) ----------------

@csrf_exempt
@role_required("admin")
def update_leave_view(request, leave_id):
    leave = get_leave(leave_id)
    if request.method == "POST":
        new_status = request.POST.get("status")
        update_leave_status(leave_id, new_status)
        return redirect("/leave/list/")

    # GET Request → just show the form
    return render(request, "leave/update.html", {"leave": leave})

# ---------------- Delete Leave (Admin only) ----------------

@role_required("admin")
def delete_leave_view(request, leave_id):
    delete_leave(leave_id)
    return redirect("/leave/list/")

# ---------------- View Single Leave ----------------

@role_required("admin", "staff")
def get_leave_view(request, leave_id):
    leave = get_leave(leave_id)
    role = request.session.get("role")
    return render(request, "leave/view.html", {"leave": leave, "role": role})
