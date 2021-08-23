from django.urls import path

from notifications import views as notification_view

app_name = "notifications"

urlpatterns = [
    path("", notification_view.notification_list_view, name="notifications"),
    path(
        "show/<notification_id>/",
        notification_view.notification_detail_view,
        name="notification-detail",
    ),
    path(
        "delete/<notification_id>/",
        notification_view.notification_delete_view,
        name="notification-delete",
    ),
]
