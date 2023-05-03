from django.shortcuts import render
from django.views import generic

# Create your views here.

class luchadoresList(generic.TemplateView):
    template_name = 'luchadores/luchadoresList.html'