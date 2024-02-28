from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(
        self,
        phone_number=None,
        password=None,
        username=None,
        is_superuser=False,
        is_staff=False,
        **extra_fields
    ):
        if not phone_number:
            raise ValueError('Укажите номер телефона.')

        extra_fields.setdefault("is_superuser", is_superuser)
        extra_fields.setdefault("is_staff", is_staff)
        extra_fields.setdefault("is_active", True)

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, phone_number=None, password=None, username=None, **extra_fields
    ):
        return self._create_user(
            phone_number=phone_number,
            password=password,
            username=username,
            **extra_fields
        )

    def create_superuser(
        self, phone_number=None, password=None, username=None, **extra_fields
    ):
        return self._create_user(
            phone_number=phone_number,
            password=password,
            username=username,
            is_superuser=True,
            is_staff=True,
            **extra_fields
        )
