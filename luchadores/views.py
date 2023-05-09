from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from luchadores.forms import LuchadorForm

from .models import Luchador, PAISES
from bases.views import actualizar_registros

# Create your views here.

class luchadoresList(LoginRequiredMixin, generic.ListView):
    model = Luchador
    template_name = 'luchadores/luchadoresList.html'
    login_url = 'bases:login'
    actualizar_registros()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['luchadores'] = Luchador.objects.filter(creator = self.request.user).order_by("-victorias", "derrotas")
        return context

class LuchadorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Luchador
    form_class = LuchadorForm
    success_url = reverse_lazy('luchadores:luchadores-list')
    template_name = 'luchadores/luchadoresForm.html'
    login_url = 'bases:login'
    actualizar_registros()

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.pais = PAISES[form.instance.pais]
        return super().form_valid(form)


class LuchadorEditView(LoginRequiredMixin, generic.UpdateView):
    model=Luchador
    form_class = LuchadorForm
    template_name = 'luchadores/luchadoresForm.html'
    context_object_name="obj"
    login_url = 'bases:login'
    success_url=reverse_lazy("luchadores:luchadores-list")
    actualizar_registros()
    
    def form_valid(self, form):
        form.instance.pais = PAISES[form.instance.pais]
        return super().form_valid(form)
        
    
class LuchadorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Luchador
    template_name = 'luchadores/luchadoresDelete.html'
    context_object_name = "obj"
    login_url = 'bases:login'
    success_url=reverse_lazy("luchadores:luchadores-list")
    actualizar_registros()
    
    
class LuchadorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Luchador
    login_url = 'bases:login'
    template_name = 'luchadores/luchadoresDetail.html'
    actualizar_registros()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["balanceText"] = ['Victorias', 'Empates', 'Derrotas']
        context['balance'] = [self.get_object().victorias, self.get_object().empates, self.get_object().derrotas]
        
        context["golpesText"] = ['Acertados', 'Evitados', 'Fallados', 'Recibidos']
        context['golpes'] = [self.get_object().golpes_acertados, self.get_object().golpes_evitados, self.get_object().golpes_fallados, self.get_object().golpes_encajados]
        return context
    