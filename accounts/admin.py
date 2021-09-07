from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, Subscription, User


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "membership", "stripe_customer_id", "profile_pic"]


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["profile", "stripe_subscription_id", "is_active"]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
