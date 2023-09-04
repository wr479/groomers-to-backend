import pdb

from django.views import generic
from core import models, mixins
from django.views import View
import json
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template import loader
from django.template.context_processors import csrf


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
        data = request.body
        pdb.set_trace()

        # if data.get('type') == 'callback':
    #             result = create_order(['name', 'phone'], data, 'Обратный звонок')

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
