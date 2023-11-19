from modeltranslation.translator import TranslationOptions, translator
from banquets.models import BanquetCard, Banquet, FeaturesOfTheBanquetHall, KitchenType


class BanquetCardTranslationOptions(TranslationOptions):
    fields = ["name", 'working_time', "address"]


translator.register(BanquetCard, BanquetCardTranslationOptions)


class BanquetTranslationOptions(TranslationOptions):
    fields = ["name", 'description']


translator.register(Banquet, BanquetTranslationOptions)


class FeaturesOfTheBanquetHallTranslationOptions(TranslationOptions):
    fields = ['features_name']


translator.register(FeaturesOfTheBanquetHall, FeaturesOfTheBanquetHallTranslationOptions)


class KitchenTypeTranslationOptions(TranslationOptions):
    fields = ['kitchen_type']


translator.register(KitchenType, KitchenTypeTranslationOptions)