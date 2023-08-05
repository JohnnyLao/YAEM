from modeltranslation.translator import translator, TranslationOptions
from main.models import Client, City, Food_type2, Dish


class ClientTranslationOptions(TranslationOptions):
    fields = ['description', 'address']
translator.register(Client, ClientTranslationOptions)


class CityTranslationOptions(TranslationOptions):
    fields = ['name']
translator.register(City, CityTranslationOptions)


class Food_type2TranslationOptions(TranslationOptions):
    fields = ['name']
translator.register(Food_type2, Food_type2TranslationOptions)


class DishTranslationOptions(TranslationOptions):
    fields = ['name', 'description']
translator.register(Dish, DishTranslationOptions)