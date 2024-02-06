from django.db.models import IntegerChoices, TextChoices


class HallNumber(IntegerChoices):
    HALL_1 = 1, "Зал 1"
    HALL_2 = 2, "Зал 2"
    HALL_3 = 3, "Зал 3"
    HALL_4 = 4, "Зал 4"
    HALL_5 = 5, "Зал 5"


class ParkingType1(TextChoices):
    GUARDED_RU = "Охраняемая", "Охраняемая"
    GUARDED_EN = "Guarded", "Guarded"
    GUARDED_KK = "Қорғалған", "Қорғалған"

    UNGUARDED_RU = "Неохраняемая", "Неохраняемая"
    UNGUARDED_EN = "Unguarded", "Unguarded"
    UNGUARDED_KK = "Күзетсіз", "Күзетсіз"


class ParkingType2(TextChoices):
    PAID_RU = "Платная", "Платная"
    PAID_EN = "Paid", "Paid"
    PAID_KK = "Ақылы", "Ақылы"

    FREE_RU = "Бесплатная", "Бесплатная"
    FREE_EN = "Free", "Free"
    FREE_KK = "Тегін", "Тегін"
