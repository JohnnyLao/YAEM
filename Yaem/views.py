from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


# 404 view
@cache_page(60 * 60 * 5)
def page_not_found_view(request, exception):
    return render(request, "main/404.html", status=404)


# robots txt view
@cache_page(60 * 60 * 5)
def robots_txt_view(request):
    with open('main/templates/main/robots.txt', 'r') as file:
        robots_file_content = file.read()
    return HttpResponse(robots_file_content, content_type='text')


@cache_page(60 * 60 * 5)
def sitemap_xml_view(request):
    with open('main/templates/main/sitemap.xml', 'r') as file:
        sitemap_file_content = file.read()
    return HttpResponse(sitemap_file_content, content_type='application/xml')
