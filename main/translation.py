from modeltranslation.translator import TranslationOptions, translator

from main.models import City, Client, Dish, Food_type2


class ClientTranslationOptions(TranslationOptions):
    fields = ["description", "address"]


translator.register(Client, ClientTranslationOptions)


class CityTranslationOptions(TranslationOptions):
    fields = ["name"]


translator.register(City, CityTranslationOptions)


class Food_type2TranslationOptions(TranslationOptions):
    fields = ["name"]


translator.register(Food_type2, Food_type2TranslationOptions)


class DishTranslationOptions(TranslationOptions):
    fields = ["name", "description"]


translator.register(Dish, DishTranslationOptions)
