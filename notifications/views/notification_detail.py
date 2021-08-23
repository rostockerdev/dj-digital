from django.shortcuts import render

from notifications.models import Notification


def notification_detail_view(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.viewed = True
    notification.save()
    return render(
        request,
        "notifications/notifications_detail.html",
        {"notification": notification},
    )
