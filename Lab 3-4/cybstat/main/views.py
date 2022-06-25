from django.shortcuts import render, redirect
from .models import CybdbModels
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


def logout_user(request):
    logout(request)
    return redirect('index')


class About(TemplateView):
    template_name = 'main/about.html'


class Cart(TemplateView):
    template_name = 'main/cart.html'


class Log(TemplateView):
    template_name = 'main/log.html'


    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context['error'] = "Неправильный логин или пароль"
        return render(request, self.template_name, context)


def index(request):
    players = CybdbModels.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная', 'CybdbModels': players})


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










