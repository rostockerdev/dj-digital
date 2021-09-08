import simplejson as json
from django.http import HttpResponse
from haystack.query import SearchQuerySet


def search_query_auto_complete_view(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get("q", ""))
    suggestions = [result.title for result in sqs]
    the_data = json.dumps({"results": suggestions})
    return HttpResponse(the_data, content_type="application/json")
