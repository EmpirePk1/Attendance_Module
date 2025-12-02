from django.shortcuts import render, redirect
from ..services.admin_service import (
    create_admin, get_admin_by_id, list_admins, update_admin, delete_admin
)
from ..utils.decorators import role_required

@role_required("admin")
def list_admins_view(request):
    admins = list_admins()
    return render(request, "admin/list.html", {"admins": admins})

@role_required("admin")
def create_admin_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        create_admin(name, email, password)
        return redirect("/admin/list/")
    return render(request, "admin/create.html")

@role_required("admin")
def update_admin_view(request, admin_id):
    admin = get_admin_by_id(admin_id)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        update_admin(admin_id, name=name, email=email)
        return redirect("/admin/list/")
    return render(request, "admin/update.html", {"admin": admin})

@role_required("admin")
def delete_admin_view(request, admin_id):
    delete_admin(admin_id)
    return redirect("/admin/list/")
