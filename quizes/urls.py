from django.urls import path

from quizes.views.quiz_view import quiz_view

app_name = "quizes"

urlpatterns = [path("", quiz_view, name="quiz")]
