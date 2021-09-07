from django.contrib import admin

from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ("title", "notification_at", "message", "is_viewed", "user")
    list_filter = ["is_viewed", "notification_at"]


admin.site.register(Notification, NotificationAdmin)
