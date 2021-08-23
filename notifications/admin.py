from django.contrib import admin

from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ("title", "notification_at", "message", "viewed", "user")
    list_filter = ["viewed", "notification_at"]


admin.site.register(Notification, NotificationAdmin)
