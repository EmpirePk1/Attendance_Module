from django.shortcuts import render, redirect
from ..services.staff_service import (
    create_staff, get_staff_by_id, list_staff, update_staff, delete_staff
)
from ..utils.decorators import role_required

# Admin-only views
@role_required("admin")
def list_staff_view(request):
    staff_list = list_staff()
    return render(request, "staff/list.html", {"staff_list": staff_list})

@role_required("admin")
def create_staff_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        department_id = request.POST.get("department_id")
        gender = request.POST.get("gender")
        profile_pic = request.FILES.get("profile_pic")
        create_staff(name, email, phone, password, department_id, gender, profile_pic)
        return redirect("/staff/list/")
    return render(request, "staff/create.html")

@role_required("admin")
def update_staff_view(request, staff_id):
    staff = get_staff_by_id(staff_id)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        update_staff(staff_id, name=name, email=email, phone=phone)
        return redirect("/staff/list/")
    return render(request, "staff/update.html", {"staff": staff})

@role_required("admin")
def delete_staff_view(request, staff_id):
    delete_staff(staff_id)
    return redirect("/staff/list/")
