from django.contrib import admin

from .models import Instructor, Rating


class InstructorAdmin(admin.ModelAdmin):
    model = Instructor
    list_display = ["username", "email", "dofb", "biography"]
    list_filter = ["username", "dofb"]


class RatingAdmin(admin.ModelAdmin):
    model = Rating
    list_display = ("instructor", "rating", "user", "review", "pub_date")
    list_filter = ["pub_date", "user"]
    search_fields = ["review"]


admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Rating, RatingAdmin)
