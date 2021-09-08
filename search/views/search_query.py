from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from haystack.query import SearchQuerySet


@csrf_exempt
def search_query_view(request):
    query_text = request.GET.get("q", "")
    if query_text == "":
        return redirect("home")
    else:
        courses = SearchQuerySet().filter(content_auto=query_text)
        print(courses)
        return render(request, "search/search.html", {"courses": courses})
