from django.conf.urls import url
from question import views


urlpatterns = [
    url(r'^$', views.getQuestion, name='question'),
    url(r'^johncena/', views.getQuestion),
    url(r'^(?P<level>[0-9]+)/$', views.getQuestionByLevel, name='question_by_level'),
    url(r'^(?P<level>[0-9]+)/johncena$', views.getQuestionByLevel),
    url(r'^answer/$', views.submitAnswer, name='answer'),
]