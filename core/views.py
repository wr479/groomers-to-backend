from django.shortcuts import render
from django.views import View
from .models import TextPage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

import pdb
import requests
from django.shortcuts import render, redirect
from .forms import ApplicationForm
from core.models import *


class TextPageView(View):
    def get(self, request):
        text_page = TextPage.objects.first()
        h1, description = text_page.get_seo_data()
        context = {
            'text_page': text_page,
            'seo_h1': h1,
            'seo_description': description,
        }
        return render(request, 'index', context)


def ajax(request):
    result = False
    if request.method == 'POST':
        data = json.loads(request.body)
        if data.get('type') == 'booking':
            result = create_order(['name', 'phone'], data, 'Забронировать игру')
        if data.get('type') == 'consultation':
            result = create_order(['name', 'phone', 'comment'], data, 'Консультация')
        if data.get('type') == 'review':
            data_review = {
                "name": data.get('name'),
                "text": data.get('text'),
                "rating": data.get('rating'),
            }
            result = create_review(['name', 'text', 'rating'], data_review)

    return JsonResponse({'created': result})


def create_order(names: list, data: dict, type: str):
    obj_info = {'type': type}
    message = f'Заявка: {type}\n'
    for name in names:
        obj_info[name] = data.get(name, '')
        message += f'{Order._meta.get_field(name).verbose_name}: {data.get(name, "")}\n'
    requests.get(
        f'https://api.telegram.org/bot6205374116:AAFA4GI_wUPrw7-S2J2CbhexW6IIh-dxAvs/sendMessage?chat_id=-619794982&text={message}')
    Order.objects.create(**obj_info)
    return True


def create_review(names: list, data: dict, ):
    obj_info = {}
    for name in names:
        obj_info[name] = data.get(name, '')

    Review.objects.create(**obj_info)
    return True
