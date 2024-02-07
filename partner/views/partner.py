from django.views.generic import TemplateView


class Partner(TemplateView):
    template_name = "partner/partner.html"
