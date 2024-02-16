from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api_v1.views import ClientViewSet

app_name = "api_v1"

root_router = SimpleRouter()
root_router.register("clients", ClientViewSet, basename="clients")

urlpatterns = [
    path("", include(root_router.urls)),
]
