from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # admin URLS
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("", include("main.urls", namespace="main")),
    path("", include("partner.urls", namespace="partner")),
    path("", include("cart.urls", namespace="cart")),
    path("", include("banquets.urls", namespace="banquets")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", include("registration.urls", namespace="register")),
    prefix_default_language=False,
)

handler404 = "Yaem.views.page_not_found_view"

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
