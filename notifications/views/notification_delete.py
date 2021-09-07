from django.shortcuts import redirect

from notifications.models import Notification


def notification_delete_view(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.delete()
    return redirect("notifications:notification-list")
