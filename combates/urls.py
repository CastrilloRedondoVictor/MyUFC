from django.urls import path, include
from django.contrib.auth import views as auth_views

from combates.views import combatesList

urlpatterns = [
    path('', combatesList.as_view(), name='combatesList'),
]