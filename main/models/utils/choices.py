from django.db.models import TextChoices


class Rates(TextChoices):
    BRONZE = "БРОНЗА", "БРОНЗА"
    SILVER = "СЕРЕБРО", "СЕРЕБРО"
    GOLD = "ЗОЛОТО", "ЗОЛОТО"
