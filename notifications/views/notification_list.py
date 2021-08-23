from django.shortcuts import render

from notifications.models import Notification


def notification_list_view(request):
    notifications = (
        Notification.objects.filter(user=request.user)
        .all()
        .order_by("-notification_at")
    )
    return render(
        request,
        "notifications/notifications_list.html",
        {"notifications": notifications},
    )
