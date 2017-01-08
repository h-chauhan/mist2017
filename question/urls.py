from django.conf.urls import url
from question import views


urlpatterns = [
    url(r'^(?P<lvl>[0-9]+)/$', views.getQuestion, name='question'),
    url(r'^(?P<lvl>[0-9]+)/answer/$', views.submitAnswer, name='answer'),
]