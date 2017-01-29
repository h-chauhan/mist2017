from django.shortcuts import render, HttpResponse
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from django.contrib.auth.decorators import login_required
from ratelimit.decorators import ratelimit

# Create your views here.
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

@ratelimit(key='ip', rate='10/m')
def login(request):
    return render(request, 'login/login.html')