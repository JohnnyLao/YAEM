from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api_v1.views import banquets, main, users

app_name = "api_v1"
router = DefaultRouter()

# Register viewsets for different API endpoints

# Menu API
router.register(r"menu/clients", main.ClientViewSet, "clients")  # Endpoints for clients
router.register(r"menu/city", main.CityViewSet, "city")  # Endpoints for cities

# Banquet API
router.register(
    r"banquets/banquet", banquets.BanquetViewSet, "banquet"
)  # Endpoints for banquets

# Define urlpatterns, including the router's URLs
urlpatterns = [
    # temp path for categories list
    path('menu/categories/', main.CategoryListView.as_view()),
    # Include the URLs provided by the router
    path('', include(router.urls)),
    # Auth users
    path("auth/", include("djoser.urls.jwt")),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
