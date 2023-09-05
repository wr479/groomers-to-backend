import pdb
import json
import json
from telegram import Bot

from django.http import JsonResponse
from django.views import View
from telegram import Bot
from django.views import generic
from core import models, mixins
from django.views import View
from . import models
from ..models import YourModel
from django.http import JsonResponse
import json
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from telegram import Bot


class IndexView(mixins.TextPageMixin, generic.TemplateView):
    page_slug = "index"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["masters"] = models.Masters.objects.all()

        return context


class AboutView(mixins.TextPageMixin, generic.TemplateView):
    page_slug = "about"
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['masters'] = models.Masters.objects.all()
        return context


class PriceView(mixins.TextPageMixin, generic.TemplateView):
    page_slug = "price"
    template_name = "price.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Services'] = models.Service.objects.all()
        return context


class ReviewsView(mixins.TextPageMixin, generic.TemplateView):
    page_slug = "reviews"
    template_name = "reviews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review'] = models.Review.objects.all()
        return context


class AjaxView(View):

    async def post(self, request):
        try:
            data = json.loads(request.body)
            name = data.get('name')
            phone = data.get('phone')
            question = data.get('question')
            category = data.get('category')

            # Создайте объект модели и сохраните данные
            your_model_instance = YourModel(name=name, phone=phone, question=question, category=category)
            your_model_instance.save()

            # Отправьте сообщение в Telegram
            message = f"Новая заявка!\nИмя: {name}\nТелефон: {phone}\nВопрос: {question}\nКатегория: {category}"
            bot = Bot(token="6641574210:AAGhG8dJLEWKC520G2NuT8JbiVO4XNiRImU")
            chat_id = "-907409135"
            bot.send_message(chat_id, message)
            print("ура")
            # Верните успешный JSON-ответ
            response_data = {'message': 'Данные успешно сохранены'}
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})


def create_order(self):
    pass

#
#

#         data = json.loads(request.body)

#         if data.get('type') == 'callback':
#             result = create_order(['name', 'phone'], data, 'Обратный звонок')
#         if data.get('type') == 'consultation':
#             result = create_order(['name', 'phone', 'email', 'comment'], data, 'Консультация')
#         if data.get('type') == 'trucking':
#             result = create_order(['name', 'phone', 'dimensions', 'weight', 'city_from', 'city_to'], data,
#                                   'Расчёт грузоперевозки')
#         if data.get('type') == 'cargo':
#             result = create_order(['name', 'phone', 'email', 'comment', 'cargo', 'weight', 'city_to'], data,
#                                   'Расчёт доставки опасного груза')
#         if data.get('type') == 'cargo_product':
#             result = create_order(['name', 'phone', 'email', 'comment', 'cargo', 'weight', 'city_from', 'city_to'],
#                                   data,
#                                   'Расчёт доставки опасного груза')
#         if data.get('type') == 'application':
#             result = create_order(['name', 'phone', 'email', 'comment', 'cargo', 'weight', 'city_to'], data,
#                                   'Заявка на покупку метанола')
#         if data.get('type') == 'jobs':
#             result = create_order(['name', 'phone'], data, 'Заявка на работу')
#     return JsonResponse({'created': result})
