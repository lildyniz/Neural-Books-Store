from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, SearchHeadline

from .models import Book

def q_search(query):

    if query.isdigit() and len(query) <= 5:
        return Book.objects.filter(id=int(query))

    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    return Book.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")