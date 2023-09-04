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





