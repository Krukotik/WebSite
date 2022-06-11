from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class About(TemplateView):
    template_name = 'main/about.html'


class Index(TemplateView):
    template_name = 'main/index.html'
