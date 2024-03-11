from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.settings import api_settings

from api_v1.serializers.users import AuthTokenSerializer, UserSerializer


@extend_schema_view(
    post=extend_schema(summary="Создать пользователя", tags=["Регистрация & Аутентификация"]),
)
class CreateUserView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    queryset = get_user_model().objects.all()
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
