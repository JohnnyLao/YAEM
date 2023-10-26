from django.shortcuts import render
from django.views.generic import TemplateView


class BanquetPage(TemplateView):
    template_name = "banquets/banquet_list.html"
