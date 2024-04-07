from django.db.models import TextChoices


class Rates(TextChoices):
    BRONZE = "БРОНЗА", "БРОНЗА"
    SILVER = "СЕРЕБРО", "СЕРЕБРО"
    GOLD = "ЗОЛОТО", "ЗОЛОТО"


class PaymentStatuses(TextChoices):
    INPROCESSING = 'INPROCESSING', 'В ОБРАБОТКЕ'
    PAID = 'PAID', 'ОПЛАЧЕНО'
    CANCELLED = 'CANCELLED', 'ОТМЕНЕНО'
