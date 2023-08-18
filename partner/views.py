from .forms import FeedBackForm
from django.views.generic.edit import FormView


class Partner(FormView):
    template_name = "partner/partner.html"
    form_class = FeedBackForm

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path
