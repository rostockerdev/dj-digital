import csv

from django.contrib import admin
from django.http import HttpResponse

from courses.models import Comment, Course, Lesson, Review
from instructors.models import Instructor
from memberships.models import Membership


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = [
        "title",
        "description",
        "extra_info",
        "start_date",
        "get_liked_user",
        "get_memberships",
        "get_instructors",
    ]
    search_fields = ["title"]
    list_filter = ["start_date"]
    list_per_page = 20
    actions = ["export_courses"]

    def get_instructors(self, obj):
        return ", ".join(
            [instructor.first_name for instructor in obj.instructors.all()]
        )

    def get_memberships(self, obj):
        return ", ".join(
            [mem_type.membership_type for mem_type in obj.allowed_membership.all()]
        )

    def get_liked_user(self, obj):
        return ", ".join([likeduser.username for likeduser in obj.likes.all()])

    # def export_courses(modeladmin, request, queryset):
    def export_courses(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="course.csv"'
        writer = csv.writer(response)
        writer.writerow(
            [
                "Title",
                "Description",
                "Extra Information",
                "Start date",
                "Liked",
                "Allowed Membership",
                "Instructors",
            ]
        )
        courses = queryset.values_list(
            "title",
            "description",
            "extra_info",
            "start_date",
            "likes__username",
            "allowed_membership__membership_type",
            "instructors__username",
        )
        for course in courses:
            writer.writerow(course)
        return response

    export_courses.short_description = "Export To CSV"
    get_memberships.short_description = "Allowed Memberships"
    get_instructors.short_description = "Instructors"
    get_liked_user.short_description = "Liked"


class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "extra_info", "course"]
    # list_display = ['title', 'slug', 'description',
    #                 'start_date', 'likes', 'get_memberships']
    search_fields = ["title"]
    list_filter = ["title"]
    list_per_page = 20


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ("course", "rating", "user", "comment", "pub_date")
    list_filter = ["pub_date", "user"]
    search_fields = ["comment"]


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ("author", "msg", "comment_at", "lesson", "approved_comment")
    list_filter = ["author", "comment_at", "approved_comment"]
    search_fields = ["author", "comment_at"]
    list_per_page = 20
    actions = ["make_comment_approve"]

    def make_comment_approve(self, request, queryset):
        rows_updated = queryset.update(approved_comment=True)
        if rows_updated == 1:
            message_bit = "1 comment was"
        else:
            message_bit = f"{rows_updated} comment were"
        self.message_user(request, f"{message_bit} successfully approved")

    make_comment_approve.short_description = "Approve Users Comment"


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
