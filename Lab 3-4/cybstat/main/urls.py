from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', Index.as_view()),
    path('about', About.as_view()),
]

