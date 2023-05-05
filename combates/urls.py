from django.urls import path, include
from django.contrib.auth import views as auth_views

from combates.views import CombateListView, CombateEditView, CombateDeleteView, CombateCreateView, CombateDetailView

urlpatterns = [
    path('', CombateListView.as_view(), name='combates-list'),
    path('new', CombateCreateView.as_view(), name = 'combates_create'),
    path('edit/<uuid:pk>/', CombateEditView.as_view(), name = 'combates_edit'),
    path('delete/<uuid:pk>/', CombateDeleteView.as_view(), name='combates_delete'),
    path('detail/<uuid:pk>/', CombateDetailView.as_view(), name='combates_detail'),
]