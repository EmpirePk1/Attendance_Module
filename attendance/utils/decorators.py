# utils/decorators.py

from django.shortcuts import redirect
from functools import wraps

def role_required(*allowed_roles):
    """
    Decorator to restrict access based on user roles.
    Usage: @role_required("admin"), @role_required("staff", "admin")
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            role = request.session.get("role")
            if not role or role not in allowed_roles:
                # Redirect to login if role not allowed or not logged in
                return redirect("/login/")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
