from django.contrib import admin

from subscriptions.models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    model = Subscribe
    list_display = ("email", "status", "created_date", "updated_date")
    list_filter = ["status", "created_date"]
    search_fields = ["status", "created_date"]


admin.site.register(Subscribe, SubscribeAdmin)
