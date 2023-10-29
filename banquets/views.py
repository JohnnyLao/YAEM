from banquets.models import Banquet
from django.views.generic import TemplateView


class BanquetList(TemplateView):
    template_name = "banquets/banquet_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banquets'] = Banquet.objects.all()
        return context


class BanquetPage(TemplateView):
    template_name = "banquets/banquet_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_name = self.kwargs['url_name']
        banquet = Banquet.objects.get(url_name=url_name)
        context['banquets'] = banquet
        return context

