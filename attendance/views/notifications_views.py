from django.shortcuts import render, redirect
from ..services.notification_service import (
    create_notification,
    list_notifications,
    list_notifications_for_staff,
    get_notification,
    update_notification,
    delete_notification
)
from ..utils.decorators import role_required

# ---------------- List Notifications ----------------
@role_required("admin")
def list_notifications_view(request):
    notifications = list_notifications()
    return render(request, "notifications/list.html", {"notifications": notifications})

@role_required("staff")
def list_my_notifications_view(request):
    staff_id = request.session.get("user_id")
    notifications = list_notifications_for_staff(staff_id)
    return render(request, "notifications/list.html", {"notifications": notifications})

# ---------------- Create Notification (Admin only) ----------------
@role_required("admin")
def create_notification_view(request):
    if request.method == "POST":
        staff_id = request.POST.get("staff_id")
        message = request.POST.get("message")
        create_notification(staff_id, message)
        return redirect("/notifications/list/")
    return render(request, "notifications/create.html")

# ---------------- Get Notification Details ----------------
@role_required("admin", "staff")
def get_notification_view(request, notification_id):
    notification = get_notification(notification_id)
    if not notification:
        return redirect("/notifications/list/")
    return render(request, "notifications/detail.html", {"notification": notification})

# ---------------- Update Notification (Admin only) ----------------
@role_required("admin")
def update_notification_view(request, notification_id):
    notification = get_notification(notification_id)
    if not notification:
        return redirect("/notifications/list/")
    
    if request.method == "POST":
        staff_id = request.POST.get("staff_id")
        message = request.POST.get("message")
        update_notification(notification_id, message=message, staff_id=staff_id)
        return redirect("/notifications/list/")
    
    return render(request, "notifications/update.html", {"notification": notification})

# ---------------- Delete Notification (Admin only) ----------------
@role_required("admin")
def delete_notification_view(request, notification_id):
    delete_notification(notification_id)
    return redirect("/notifications/list/")
