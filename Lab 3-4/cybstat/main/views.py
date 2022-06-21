from django.shortcuts import render
from .models import CybdbModels
from django.views.generic import TemplateView


class About(TemplateView):
    template_name = 'main/about.html'


class Reg(TemplateView):
    template_name = 'main/reg.html'


class Log(TemplateView):
    template_name = 'main/log.html'


def index(request):
    players = CybdbModels.objects.order_by('-id')
    return render(request, 'main/index.html', {'CybdbModels': players})
