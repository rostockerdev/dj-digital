from django.urls import path

from instructors import views
from instructors.models import Instructor

app_name = "instructors"
urlpatterns = [
    path("", views.InstructorListView.as_view(), name="instructor-list"),
    path(
        "<str:instructor_name>/",
        views.InstructorDetailView.as_view(),
        name="instructor-detail",
    ),
    path("<str:instructor_name>/add-rating/", views.AddRatingView, name="add-rating"),
]
