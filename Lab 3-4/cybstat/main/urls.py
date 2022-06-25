from django.urls import path
from .views import *
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.index, name='index'),
    path('about', About.as_view()),
    path('reg', Reg.as_view()),
    path('log', Log.as_view()),
    path('cart', Cart.as_view()),
    path('logout', views.logout_user),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

