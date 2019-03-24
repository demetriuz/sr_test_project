from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^api/', include('alignment_tags.urls', namespace='alignment_tags')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index')
]
