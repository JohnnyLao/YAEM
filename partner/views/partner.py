from django.views.generic import RedirectView


class Partner(RedirectView):
    permanent = True
    url = 'https://online-menu.org/'
