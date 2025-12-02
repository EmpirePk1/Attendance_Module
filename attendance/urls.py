from django.urls import path
from .views import (
    admin_views, staff_views, departments_views,
    attendance_views, attendance_report_views,
    leave_views, feedback_views, notifications_views,
    auth_views
)

urlpatterns = [
    # ----------------- Index & Auth -----------------
    path('', auth_views.index_view, name='index'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
    path('dashboard/', auth_views.dashboard_view, name='dashboard'),

    # ----------------- Admin URLs -----------------
    path('admin/list/', admin_views.list_admins_view, name='list_admins'),
    path('admin/create/', admin_views.create_admin_view, name='create_admin'),
    path('admin/<str:admin_id>/update/', admin_views.update_admin_view, name='update_admin'),
    path('admin/<str:admin_id>/delete/', admin_views.delete_admin_view, name='delete_admin'),

    # ----------------- Staff URLs -----------------
    path('staff/list/', staff_views.list_staff_view, name='list_staff'),
    path('staff/create/', staff_views.create_staff_view, name='create_staff'),
    path('staff/<str:staff_id>/update/', staff_views.update_staff_view, name='update_staff'),
    path('staff/<str:staff_id>/delete/', staff_views.delete_staff_view, name='delete_staff'),

    # ----------------- Departments URLs -----------------
    path('departments/list/', departments_views.list_departments_view, name='list_departments'),
    path('departments/create/', departments_views.create_department_view, name='create_department'),
    path('departments/<str:department_id>/update/', departments_views.update_department_view, name='update_department'),
    path('departments/<str:department_id>/delete/', departments_views.delete_department_view, name='delete_department'),

    # ----------------- Attendance URLs -----------------
    path('attendance/list/', attendance_views.list_attendance_view, name='list_attendance'),
    path('attendance/mylist/', attendance_views.list_my_attendance_view, name='my_attendance'),
    path('attendance/<str:attendance_id>/update/', attendance_views.update_attendance_view, name='update_attendance'),
    path('attendance/<str:attendance_id>/delete/', attendance_views.delete_attendance_view, name='delete_attendance'),
    path('attendance/checkin_checkout/', attendance_views.staff_checkin_checkout_view, name='checkin_checkout'),

    # ----------------- Attendance Reports URLs -----------------
    path('attendance_reports/list/', attendance_report_views.list_attendance_reports_view, name='list_attendance_reports'),
    path('attendance_reports/mylist/', attendance_report_views.list_my_attendance_reports_view, name='my_attendance_reports'),
    path('attendance_reports/<str:report_id>/update/', attendance_report_views.update_attendance_report_view, name='update_attendance_report'),
    path('attendance_reports/<str:report_id>/delete/', attendance_report_views.delete_attendance_report_view, name='delete_attendance_report'),

    # ----------------- Leave URLs -----------------
    path('leave/list/', leave_views.list_leave_view, name='list_leave'),  # Admin: view all leaves
    path('leave/mylist/', leave_views.list_my_leave_view, name='my_leave'),  # Staff: view own leaves
    path('leave/apply/', leave_views.apply_leave_view, name='apply_leave'),
    path('leave/<str:leave_id>/update/', leave_views.update_leave_view, name='update_leave'),
    path('leave/<str:leave_id>/delete/', leave_views.delete_leave_view, name='delete_leave'),

    # ---------------- Feedback URLs -----------------
    path('feedback/list/', feedback_views.list_feedback_view, name='list_feedback'),  # Admin: all feedback
    path('feedback/create/', feedback_views.create_feedback_view, name='add_feedback'),  # Staff will add feedback
    path('feedback/mylist/', feedback_views.list_my_feedback_view, name='my_feedback'),  # Staff: own feedback
    path('feedback/<str:feedback_id>/update/', feedback_views.update_feedback_view, name='update_feedback'),  # Admin: reply/update feedback
    path('feedback/<str:feedback_id>/delete/', feedback_views.delete_feedback_view, name='delete_feedback'),


    # ----------------- Notifications URLs -----------------
    path('notifications/list/', notifications_views.list_notifications_view, name='list_notifications'),  # Admin: all notifications
    path('notifications/create/', notifications_views.create_notification_view, name='create_notifications'),
    path('notifications/mylist/', notifications_views.list_my_notifications_view, name='my_notifications'),  # Staff: own notifications
    path('notifications/<str:notification_id>/update/', notifications_views.update_notification_view, name='update_notification'),  # Admin: update notification
    path('notifications/<str:notification_id>/delete/', notifications_views.delete_notification_view, name='delete_notification'),
]
