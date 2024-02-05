from django.views.generic import TemplateView

from banquets.models import BanquetCard


class BanquetPage(TemplateView):
    template_name = "banquets/banquet_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_name = self.kwargs["url_name"]
        banquet_card = BanquetCard.objects.get(url_name=url_name)
        subhall = banquet_card.banquet_set.all()
        context["banquet"] = banquet_card
        context["subhall"] = subhall
        return context
