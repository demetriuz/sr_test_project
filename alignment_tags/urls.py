from django.urls import path

from . import views

app_name = 'alignment_tags'

urlpatterns = [
    path('levels-and-tags/', views.LevelsAndTags.as_view(), name='levels'),
]
