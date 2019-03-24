from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('levels/', views.Levels.as_view(), name='levels'),
]
