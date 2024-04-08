from modeltranslation.translator import TranslationOptions, translator

from banquets.models import Banquet, BanquetCard, FeaturesOfTheBanquetHall, KitchenType


class BanquetCardTranslationOptions(TranslationOptions):
    fields = ["name", "address"]


translator.register(BanquetCard, BanquetCardTranslationOptions)


class BanquetTranslationOptions(TranslationOptions):
    fields = ["name", "description", "parking_1", "parking_2"]


translator.register(Banquet, BanquetTranslationOptions)


class FeaturesOfTheBanquetHallTranslationOptions(TranslationOptions):
    fields = ["features_name"]


translator.register(
    FeaturesOfTheBanquetHall, FeaturesOfTheBanquetHallTranslationOptions
)


class KitchenTypeTranslationOptions(TranslationOptions):
    fields = ["kitchen_type"]


translator.register(KitchenType, KitchenTypeTranslationOptions)
