from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime 
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.views import LoginView , LogoutView

# login class 
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

# logout class 
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today' : datetime.today()}

