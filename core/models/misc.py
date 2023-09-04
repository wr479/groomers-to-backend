from django.db import models
from django.shortcuts import render


class SiteSettings(models.Model):
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    robots = models.TextField("robots.txt", blank=True)
    favicon = models.ImageField("Favicon", upload_to="favicon", blank=True)
    extra_head_html = models.TextField(blank=True)
    extra_body_html = models.TextField(blank=True)

    @classmethod
    def get(cls):
        if not hasattr(cls, "_cached_obj"):
            cls._cached_obj = cls.objects.get()
        return cls._cached_obj

    def __str__(self):
        return "Настройки сайта"


class CompanyContacts(models.Model):
    email = models.EmailField(verbose_name="E-mail", blank=True)
    phone = models.CharField(verbose_name="Телефон", max_length=16, blank=True)
    requisites = models.TextField(verbose_name="Реквизиты", blank=True)

    address = models.CharField(verbose_name="Адрес", max_length=128, blank=True)
    address_html_code = models.TextField(verbose_name="HTML код для вставки карты", blank=True)

    class Meta:
        verbose_name = "Контакты компании"
        verbose_name_plural = "Контакты компании"

    def __str__(self):
        return "Контакты компании"


class ExtraFields(models.Model):
    class Meta:
        verbose_name = "Дополнительное поле"
        verbose_name_plural = "Дополнительные поля"

    key = models.CharField(verbose_name="Ключ", help_text="", max_length=20, unique=True)
    title = models.CharField(verbose_name="Заголовок", max_length=100, blank=True)
    text = models.TextField(verbose_name="Текст", blank=True)

    def __str__(self):
        return self.title or self.key


class FeedbackRequest(models.Model):
    email = models.EmailField(verbose_name="E-mail", blank=True)
    first_name = models.CharField(max_length=64, verbose_name="Имя")
    last_name = models.CharField(max_length=64, verbose_name="Фамилия", blank=True)
    phone = models.CharField(max_length=11, verbose_name="Телефон")

    comment = models.TextField(blank=True)

    class Meta:
        verbose_name = "Заявка на обратную связь"
        verbose_name_plural = "Заявки на обратную связь"

    def __str__(self):
        return f'Заявка от {self.phone}'


class Service(models.Model):
    service_number = models.CharField(max_length=20, verbose_name="Номер услуги")
    service_name = models.CharField(max_length=100, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Цены")
    description = models.TextField(verbose_name="Описание", blank=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.service_name


# Модель описания inline полей
class ServiceDescriptions(models.Model):
    class Meta:
        verbose_name = "Описание услуги"
        verbose_name_plural = "Описания услуг"

    name = models.CharField(verbose_name="Пункт", max_length=256)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Masters(models.Model):
    name = models.CharField(max_length=256, verbose_name="ФИО")
    post = models.CharField(max_length=256, verbose_name="Должность", blank=True)
    photo = models.FileField(verbose_name="Фото", upload_to="masters")
    description = models.TextField(verbose_name="Описание", blank=True)

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"


class Order(models.Model):
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    # клиент
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=100)
    # доп инфа


    def __str__(self):
        return self.name


class Review(models.Model):
    review_name = models.CharField(max_length=256, verbose_name="ФИО")
    review_post = models.CharField(max_length=256, verbose_name="Время", blank=True)
    review_photo = models.FileField(verbose_name="Фото", upload_to="client")
    review_description = models.TextField(verbose_name="Описание", )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.review_name
