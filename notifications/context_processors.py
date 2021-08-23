from notifications.models import Notification


# Return the number of notification that user have
def notification_count(request):
    if request.user.is_authenticated:
        nc_count = Notification.objects.filter(user=request.user, viewed=False).count()
        return {"notification_count": nc_count}
    else:
        return {"notification_count": None}
