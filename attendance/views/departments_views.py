from django.shortcuts import render, redirect
from ..services.department_service import (
    create_department, get_department_by_id, list_departments,
    update_department, delete_department
)
from ..utils.decorators import role_required

@role_required("admin")
def list_departments_view(request):
    departments = list_departments()
    return render(request, "departments/list.html", {"departments": departments})

@role_required("admin")
def create_department_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        create_department(name)
        return redirect("/departments/list/")
    return render(request, "departments/create.html")

@role_required("admin")
def update_department_view(request, department_id):
    department = get_department_by_id(department_id)
    if request.method == "POST":
        name = request.POST.get("name")
        update_department(department_id, name=name)
        return redirect("/departments/list/")
    return render(request, "departments/update.html", {"department": department})

@role_required("admin")
def delete_department_view(request, department_id):
    delete_department(department_id)
    return redirect("/departments/list/")
