from django.conf import settings
from django.contrib import admin

from twilio.rest import Client

from .models import Instructor, Rating


def twilio_text(modelAdmin, request, queryset):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for instructor in queryset:
        client.messages.create(
            to=str(instructor.mobile_no),
            from_=settings.TWILIO_PHONE_NO,
            body="Hey I hope received this message",
        )


twilio_text.short_description = "Send Text"


class InstructorAdmin(admin.ModelAdmin):
    model = Instructor
    list_display = ["username", "email", "dofb", "mobile_no", "biography"]
    list_filter = ["username", "dofb"]

    actions = [twilio_text]


class RatingAdmin(admin.ModelAdmin):
    model = Rating
    list_display = ("instructor", "rating", "user", "review", "pub_date")
    list_filter = ["pub_date", "user"]
    search_fields = ["review"]


admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Rating, RatingAdmin)
