from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'emails'

urlpatterns = [
    path('', views.index, name="index"),
    path('wsSendEmail', views.wsSendEmail, name="wsSendEmail"),
    path('vista', views.msj, name="vista")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
