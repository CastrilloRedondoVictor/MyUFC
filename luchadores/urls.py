from django.urls import path, include
from django.contrib.auth import views as auth_views

from luchadores.views import luchadoresList

urlpatterns = [
    path('', luchadoresList.as_view(), name='luchadoresList'),
]