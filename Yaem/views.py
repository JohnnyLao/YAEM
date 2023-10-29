from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(60 * 60 * 5)
def page_not_found_view(request, exception):
    return render(request, "main/404.html", status=404)
