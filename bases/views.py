from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from luchadores.models import Luchador
from combates.models import Combate

# Create your views here.

def actualizar_registros():
    for luchador in Luchador.objects.all():
        luchador.victorias = 0
        luchador.derrotas = 0
        luchador.empates = 0
        luchador.golpes_acertados = 0
        luchador.golpes_totales = 0
        luchador.golpes_fallados = 0
        luchador.save()
        
        for combate in Combate.objects.all():
            
            resultado = combate.resultado
            
            if luchador == combate.luchador_rojo:
                if resultado == 'rojo':
                    luchador.victorias = luchador.victorias + 1
                if resultado == 'azul':
                    luchador.derrotas = luchador.derrotas + 1
                if resultado == 'empate':
                    luchador.empates = luchador.empates + 1
                    
                luchador.golpes_acertados = luchador.golpes_acertados + combate.golpes_acertados_rojo
                luchador.golpes_totales = luchador.golpes_totales + combate.golpes_rojo
                luchador.golpes_fallados = luchador.golpes_fallados + combate.golpes_fallados_rojo
                    
            if luchador == combate.luchador_azul:
                if resultado == 'rojo':
                    luchador.derrotas = luchador.victorias + 1
                if resultado == 'azul':
                    luchador.victorias = luchador.derrotas + 1
                if resultado == 'empate':
                    luchador.empates = luchador.empates + 1
                    
                luchador.golpes_acertados = luchador.golpes_acertados + combate.golpes_acertados_azul
                luchador.golpes_totales = luchador.golpes_totales + combate.golpes_azul
                luchador.golpes_fallados = luchador.golpes_fallados + combate.golpes_fallados_azul
                    
            luchador.save()

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = '/login'
    actualizar_registros()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        luchadores = Luchador.objects.filter(creator = self.request.user).order_by("-victorias")
        numLuchadores = luchadores.count()
        context['user'] = self.request.user.username
        if numLuchadores > 0:
            context["primero"] = luchadores[0]
            if numLuchadores > 1:
                context["segundo"] = luchadores[1]
            if numLuchadores > 2:
                context["tercero"] = luchadores[2]
        return context
    
