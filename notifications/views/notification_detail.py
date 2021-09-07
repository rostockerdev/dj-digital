from django.shortcuts import render

from notifications.models import Notification


def notification_detail_view(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.is_viewed = True
    notification.save()
    return render(
        request,
        "notifications/notification_detail.html",
        {"notification": notification},
    )
