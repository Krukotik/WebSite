from django.shortcuts import render
from .models import CybdbModels
from django.views.generic import TemplateView


class About(TemplateView):
    template_name = 'main/about.html'


def index(request):
    players = CybdbModels.objects.order_by('-id')
    return render(request, 'main/index.html', {'CybdbModels': players})

