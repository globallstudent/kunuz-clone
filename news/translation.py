# modeltranslation removed for Django 5.x compatibility
# from modeltranslation.translator import register, TranslationOptions
from news.models import News

# @register(News)
# class NewsTranslationOptions(TranslationOptions):
#     fields = ("title", "content")
