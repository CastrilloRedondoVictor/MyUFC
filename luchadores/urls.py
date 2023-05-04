from django.urls import path, include
from django.contrib.auth import views as auth_views

from luchadores.views import luchadoresList, LuchadorCreateView, LuchadorEditView, LuchadorDeleteView, LuchadorDetailView

urlpatterns = [
    path('', luchadoresList.as_view(), name='luchadores-list'),
    path('new', LuchadorCreateView.as_view(), name = 'luchadores_create'),
    path('edit/<uuid:pk>/', LuchadorEditView.as_view(), name = 'luchadores_edit'),
    path('delete/<uuid:pk>/', LuchadorDeleteView.as_view(), name='luchadores_delete'),
    path('detail/<uuid:pk>/', LuchadorDetailView.as_view(), name='luchadores_detail'),
]