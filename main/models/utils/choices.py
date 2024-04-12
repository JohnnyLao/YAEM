from django.db.models import TextChoices


class Rates(TextChoices):
    TEST = 'ТЕСТ', 'ТЕСТ'
    BRONZE = "БРОНЗА", "БРОНЗА"
    SILVER = "СЕРЕБРО", "СЕРЕБРО"
    GOLD = "ЗОЛОТО", "ЗОЛОТО"


class PaymentStatuses(TextChoices):
    INPROCESSING = 'В ОБРАБОТКЕ', 'В ОБРАБОТКЕ'
    PAID = 'ОПЛАЧЕНО', 'ОПЛАЧЕНО'
    CANCELLED = 'ОТМЕНЕНО', 'ОТМЕНЕНО'
