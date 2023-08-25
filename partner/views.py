# from .forms import FeedBackForm
from django.contrib import messages
from django.utils.translation import gettext
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

# class Partner(FormView):
#     template_name = "partner/partner.html"
#     form_class = FeedBackForm
#
#     def form_valid(self, form):
#         form.send_email()
#         messages.success(self.request, gettext('Спасибо, мы свяжемся с вами в ближайшее время!'))
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return self.request.path


class Partner(TemplateView):
    template_name = "partner/partner.html"
