from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CombateForm

from .models import Combate

from bases.views import actualizar_registros

# Create your views here.

class CombateListView(LoginRequiredMixin, generic.ListView):
    model = Combate
    template_name = 'combates/combatesList.html'
    login_url = 'bases:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actualizar_registros()
        context['combates'] = Combate.objects.filter(creator = self.request.user).order_by("-fecha")
        return context

class CombateCreateView(LoginRequiredMixin, generic.CreateView):
    model = Combate
    form_class = CombateForm
    success_url = reverse_lazy('combates:combates-list')
    template_name = 'combates/combatesForm.html'
    login_url = 'bases:login'
    actualizar_registros()

    def form_valid(self, form):
        form.instance.creator = self.request.user
        
        golpes_rojo = form.instance.golpes_directos_rojo + form.instance.golpes_crochet_rojo + form.instance.golpes_gancho_rojo
        golpes_azul = form.instance.golpes_directos_azul + form.instance.golpes_crochet_azul + form.instance.golpes_gancho_azul
        form.instance.golpes_rojo = form.instance.golpes_directos_rojo + form.instance.golpes_crochet_rojo + form.instance.golpes_gancho_rojo
        form.instance.golpes_azul = form.instance.golpes_directos_azul + form.instance.golpes_crochet_azul + form.instance.golpes_gancho_azul
        
        form.instance.golpes_fallados_rojo = golpes_rojo - form.instance.golpes_acertados_rojo
        form.instance.golpes_fallados_azul = golpes_azul - form.instance.golpes_acertados_azul
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(CombateCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CombateEditView(LoginRequiredMixin, generic.UpdateView):
    model=Combate
    form_class = CombateForm
    template_name = 'combates/combatesForm.html'
    context_object_name="obj"
    login_url = 'bases:login'
    success_url=reverse_lazy("combates:combates-list")
    actualizar_registros()
    
    def form_valid(self, form):
        golpes_rojo = form.instance.golpes_directos_rojo + form.instance.golpes_crochet_rojo + form.instance.golpes_gancho_rojo
        golpes_azul = form.instance.golpes_directos_azul + form.instance.golpes_crochet_azul + form.instance.golpes_gancho_azul
        
        form.instance.golpes_rojo = form.instance.golpes_directos_rojo + form.instance.golpes_crochet_rojo + form.instance.golpes_gancho_rojo
        form.instance.golpes_azul = form.instance.golpes_directos_azul + form.instance.golpes_crochet_azul + form.instance.golpes_gancho_azul
        
        form.instance.golpes_fallados_rojo = golpes_rojo - form.instance.golpes_acertados_rojo
        form.instance.golpes_fallados_azul = golpes_azul - form.instance.golpes_acertados_azul
        return super().form_valid(form)
        
    
class CombateDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Combate
    template_name = 'combates/combatesDelete.html'
    context_object_name = "obj"
    login_url = 'bases:login'
    success_url=reverse_lazy("combates:combates-list")
    actualizar_registros()
    
    
class CombateDetailView(LoginRequiredMixin, generic.DetailView):
    model = Combate
    login_url = 'bases:login'
    template_name = 'combates/combatesDetail.html'
    actualizar_registros()