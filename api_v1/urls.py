from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_v1.views import banquets, main, users

app_name = "api_v1"

router = DefaultRouter()
# menu api
router.register(r"menu/clients", main.ClientViewSet, "clients")
router.register(r"menu/city", main.CityViewSet, "city")
# banquet api
router.register(r"banquets/banquet", banquets.BanquetViewSet, "banquet")

urlpatterns = [
    path('user/create/', users.CreateUserView.as_view(), name='user-create'),
    path('user/token/', users.CreateTokenView.as_view(), name='user-token'),
    path('', include(router.urls)),
]
