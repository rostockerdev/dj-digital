from django.urls import path

from search.views.search_query import search_query_view
from search.views.search_query_auto import search_query_auto_complete_view

app_name = "search"

urlpatterns = [
    path("", search_query_view, name="search"),
    path("autocomplete/", search_query_auto_complete_view, name="searchauto"),
]
