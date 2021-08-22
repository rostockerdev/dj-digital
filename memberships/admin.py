from django.contrib import admin

from .models import Membership


class MembershipAdmin(admin.ModelAdmin):
    list_display = ["slug", "membership_type", "stripe_plan_id", "price"]
    list_filter = ["stripe_plan_id"]


admin.site.register(Membership, MembershipAdmin)
