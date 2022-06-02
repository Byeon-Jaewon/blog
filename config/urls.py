"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.utils import timezone
from django.views.generic import TemplateView
import random

class HomeView(TemplateView):
    template_name='index.html'
    context_object_name= 'object'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        import socket
        value = 0
        while value < 10000:
            value = random.randint(0,20000)

        try:
            HOSTNAME = socket.gethostname()
        except:
            HOSTNAME = 'localhost'
        context['hostinfo'] = HOSTNAME
        context['now'] = now
        context['ex'] = ex
        
        return context

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path('blog/', include('blog.urls'), name="blog")
]
