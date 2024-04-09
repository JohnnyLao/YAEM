from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api_v1.views import banquets, main, users

app_name = "api_v1"
router = DefaultRouter()

# Register viewsets for different API endpoints

# Menu API
# Endpoints for clients
router.register(r"menu/clients", main.ClientViewSet, "clients")
# Endpoints for categories
router.register(r'menu/categories', main.CategoryViewSet, 'categories')
# Endpoints for subcategories
router.register(r'menu/subcategories', main.SubcategoryViewSet, 'subcategories')
# Endpoints for dishes
router.register(r'menu/dishes', main.DishViewSet, 'dishes')
# Endpoints for cities
router.register(r"menu/city", main.CityViewSet, "city")
# Endpoints for payments
router.register(r"auth/payment", users.PaymentViewSet, "city")
# Endpoints for rates
router.register(r"menu/rates", main.EstablishmentRatesViewSet, "rates")


# Define urlpatterns, including the router's URLs
urlpatterns = [
    # Include the URLs provided by the router
    path('', include(router.urls)),
    # Auth users
    path("auth/", include("djoser.urls.jwt")),
    path('auth/create', users.UserRegistrationView.as_view()),
    path('auth/phone-number', users.UserPhoneNumberView.as_view()),
]
