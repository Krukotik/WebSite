from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.index),
    path('about', About.as_view()),
    path('reg', Reg.as_view()),
    path('log', Log.as_view()),
]

