from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'home/', views.home, name='home'),
]