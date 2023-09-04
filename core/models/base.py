import datetime

from django.db import models


class BaseSEOModel(models.Model):
    class Meta:
        abstract = True

    slug = models.SlugField("Slug", unique=True)

    show_in_sitemap = models.BooleanField(default=True, verbose_name="Показывать в карте сайта")

    og_title = models.CharField(max_length=200, verbose_name="OG Title", blank=True)
    og_description = models.TextField(max_length=2000, verbose_name="OG Description", blank=True)
    og_type = models.CharField(max_length=200, verbose_name="OG Type", blank=True)
    og_type_pb_time = models.DateField(default=datetime.date.today, verbose_name="Время публикации")
    og_type_author = models.CharField(max_length=200, verbose_name="OG author", blank=True)

    seo_h1 = models.CharField(max_length=200, verbose_name="H1", blank=True)
    seo_title = models.CharField(max_length=200, verbose_name="Title", blank=True)
    seo_description = models.CharField(max_length=500, verbose_name="Description", blank=True)
    seo_keywords = models.CharField(max_length=500, verbose_name="Keywords", blank=True)

    price_title = models.CharField(max_length=200, verbose_name="Price title", blank=True)
    price_money = models.CharField(max_length=200, verbose_name="money", blank=True)
    price_description = models.TextField(max_length=2000, verbose_name="Price description", blank=True)


class BaseMenuItemModel(models.Model):
    class Meta:
        abstract = True

    menu_title = models.CharField(max_length=200, verbose_name="Название в меню", blank=True)
    menu_position = models.IntegerField(verbose_name="Позиция в меню", blank=True)
