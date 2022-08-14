from termios import VINTR
from django.urls import path
from . import views


urlpatterns = [
    path('halp/', views.say_halp)
]