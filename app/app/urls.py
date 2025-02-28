"""app URL Configuration

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
from django.urls import path
from core.views import main_page
from password_generator.views import (
    password_generator_view,
    password_generator_page_view,
)
from timer.views import (
    timer_view,
    timer_api_view,
    stopwatch_api_view,
)
from tictactoe.views import tictactoe_view
from qr_coder.views import qr_code_view
from hangman.views import hangman_view
from api_weather.views import weather_view
from background_remover.views import background_remover_view

urlpatterns = [
    path('', main_page, name='main-page'),
    path('admin/', admin.site.urls),
    path('timer/', timer_view, name='timer'),
    path('generate-password/', password_generator_page_view, name='generate-password'),  # noqa
    path('tictactoe/', tictactoe_view, name='tictactoe'),
    path('qr-coder/', qr_code_view, name='qr-coder'),
    path('hangman/', hangman_view, name='hangman'),
    path('weather/', weather_view, name='weather'),
    path('background-remover', background_remover_view, name='background-remover'),  # noqa
    path('api/generate-password/', password_generator_view, name='generate-password-api'),  # noqa
    path('api/timer/', timer_api_view, name='timer-api-view'),
    path('api/stopwatch/',stopwatch_api_view, name='stopwatch'),
]
