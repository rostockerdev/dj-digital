from django.urls import path

from notifications import views as notification_view

app_name = "notifications"

urlpatterns = [
    path("", notification_view.notification_list_view, name="notification-list"),
    path(
        "show/<int:notification_id>/",
        notification_view.notification_detail_view,
        name="notification-detail",
    ),
    path(
        "delete/<int:notification_id>/",
        notification_view.notification_delete_view,
        name="notification-delete",
    ),
]
