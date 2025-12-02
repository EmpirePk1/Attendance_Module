from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from ..services.feedback_service import (
    list_feedbacks,
    list_feedback_for_staff,
    get_feedback,
    update_feedback,
    delete_feedback,
    create_feedback_report
)
from ..utils.decorators import role_required

# ---------------- List Feedbacks ----------------
@role_required("admin")
def list_feedback_view(request):
    feedbacks = list_feedbacks()
    return render(request, "feedback/list.html", {"feedbacks": feedbacks, "role": "admin"})

@role_required("staff")
def list_my_feedback_view(request):
    staff_id = request.session.get("user_id")
    feedbacks = list_feedback_for_staff(staff_id)
    return render(request, "feedback/list.html", {"feedbacks": feedbacks, "role": "staff"})

# ---------------- View Single Feedback ----------------
@role_required("admin", "staff")
def get_feedback_view(request, feedback_id):
    feedback = get_feedback(feedback_id)
    role = request.session.get("role")
    return render(request, "feedback/view.html", {"feedback": feedback, "role": role})

# ---------------- Update Feedback (Admin only) ----------------
@csrf_exempt
@role_required("admin")
def update_feedback_view(request, feedback_id):
    feedback = get_feedback(feedback_id)
    if request.method == "POST":
        reply = request.POST.get("feedback_reply")
        update_feedback(feedback_id, feedback_reply=reply)
        return redirect("/feedback/list/")
    return render(request, "feedback/update.html", {"feedback": feedback})

# ---------------- Delete Feedback (Admin only) ----------------
@role_required("admin")
def delete_feedback_view(request, feedback_id):
    delete_feedback(feedback_id)
    return redirect("/feedback/list/")

# ---------------- Create Feedback (Staff only) ----------------
@csrf_exempt
@role_required("staff")
def create_feedback_view(request):
    if request.method == "POST":
        staff_id = request.session.get("user_id")
        feedback_text = request.POST.get("feedback")
        create_feedback_report(staff_id, feedback_text, feedback_reply="")
        return redirect("/feedback/list/")
    return render(request, "feedback/create.html")
