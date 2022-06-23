from django.shortcuts import render, redirect
from .models import CybdbModels
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse



class About(TemplateView):
    template_name = 'main/about.html'


class Log(TemplateView):
    template_name = 'main/log.html'


def index(request):
    players = CybdbModels.objects.order_by('-id')
    return render(request, 'main/index.html', {'CybdbModels': players})


class Reg(TemplateView):
    template_name = "main/reg.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse('index'))

        return render(request, self.template_name)








