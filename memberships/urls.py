from django.urls import path

from memberships.views.dashboard_view import dashboard_view

app_name = "memberships"

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
]
