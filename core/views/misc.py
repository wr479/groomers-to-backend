import requests
from django.views import generic
from core import models, mixins
from . import models
from ..models import YourModel
import json
from django.http import JsonResponse
from django.views import View
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

    def post(self, request):
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

            # Отправка сообщения в Telegram с использованием библиотеки requests
            token = "6641574210:AAGhG8dJLEWKC520G2NuT8JbiVO4XNiRImU"
            chat_id = "-907409135"
            telegram_api_url = f"https://api.telegram.org/bot{token}/sendMessage"
            params = {'chat_id': chat_id, 'text': message}
            response = requests.get(telegram_api_url, params=params)

            # Проверяем успешность отправки сообщения
            if response.status_code == 200:
                # Верните успешный JSON-ответ
                response_data = {'message': 'Данные успешно сохранены'}
                return JsonResponse(response_data)
            else:
                # Если отправка не удалась, верните соответствующий ответ
                return JsonResponse({'success': False, 'error': 'Ошибка при отправке в Telegram'})

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
