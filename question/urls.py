from django.conf.urls import url
from question import views


urlpatterns = [
    url(r'^$', views.getQuestion, name='question'),
    url(r'^answer/$', views.submitAnswer, name='answer'),
]