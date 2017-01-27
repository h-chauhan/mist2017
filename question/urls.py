from django.conf.urls import url
from question import views


urlpatterns = [
    url(r'^$', views.getQuestion, name='question'),
    url(r'^(?P<level>[0-9]+)/$', views.getQuestionByLevel, name='question_by_level'),
    url(r'^answer/$', views.submitAnswer, name='answer'),
]