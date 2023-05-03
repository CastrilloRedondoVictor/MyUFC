from django.urls import path, include
from django.contrib.auth import views as auth_views

from bases.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]