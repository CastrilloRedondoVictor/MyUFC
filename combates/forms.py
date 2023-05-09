from django import forms
from .models import Combate
from luchadores.models import Luchador

class CombateForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.SelectDateWidget(
        attrs={'class': 'form-control datepicker_input'}, years=[y for y in range(1950,2023)]))
    class Meta:
        model = Combate
        fields = ['luchador_rojo', 'luchador_azul', 'fecha', 'round_max', 'resultado', 
                    'golpes_acertados_rojo', 
                    'golpes_directos_rojo', 'golpes_crochet_rojo', 'golpes_gancho_rojo',
                    'golpes_acertados_azul',
                    'golpes_directos_azul', 'golpes_crochet_azul', 'golpes_gancho_azul']
        
        widgets = {
            'luchador_rojo': forms.Select(attrs={'class': 'form-control'}),
            'luchador_azul': forms.Select(attrs={'class': 'form-control'}),
            'round_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'resultado': forms.Select(attrs={'class': 'form-control'}),
            'golpes_acertados_rojo': forms.NumberInput(attrs={'class': 'form-control'}),
            'golpes_directos_rojo': forms.NumberInput(attrs={'class': 'form-control'}),
            'golpes_crochet_rojo': forms.NumberInput(attrs={'class': 'form-control'}),
            'golpes_gancho_rojo': forms.NumberInput(attrs={'class': 'form-control'}),
            'golpes_acertados_azul': forms.NumberInput(attrs={'class': 'form-control'}),
            'golpes_directos_azul': forms.NumberInput(attrs={'class': 'form-control'}),
            'golpes_crochet_azul': forms.NumberInput(attrs={'class': 'form-control'}),
            'golpes_gancho_azul': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'luchador_rojo': 'Luchador Rojo',
            'luchador_azul': 'Luchador Azul',
            'round_max': 'Rondas Totales',
            'resultado': 'Ganador del Combate',
            'golpes_acertados_rojo': 'Golpes Acertados Rojo',
            'golpes_directos_rojo': 'Golpes Directos Rojo',
            'golpes_crochet_rojo': 'Golpes Crochet Rojo',
            'golpes_gancho_rojo': 'Golpes Gancho Rojo',
            'golpes_acertados_azul': 'Golpes Acertados Azul',
            'golpes_directos_azul': 'Golpes Directos Azul',
            'golpes_crochet_azul': 'Golpes Crochet Azul',
            'golpes_gancho_azul': 'Golpes Gancho Azul',
        }
    
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            luchadores = Luchador.objects.filter(creator=user)
            self.fields['luchador_rojo'].queryset = luchadores
            self.fields['luchador_azul'].queryset = luchadores
            
    def clean_round_max(self):
        round_max = self.cleaned_data['round_max']
        if round_max > 3:
            raise forms.ValidationError('El máximo de rondas es de 3', code='invalid_round_max')
        return round_max
    
    def clean_golpes_azul(self):
        golpes_acertados_azul = self.cleaned_data['golpes_acertados_azul']
        golpes = self.cleaned_data['golpes_directos_azul'] + self.cleaned_data['golpes_crochet_azul'] + self.cleaned_data['golpes_gancho_azul']
        
        if  golpes_acertados_azul > golpes:
            raise forms.ValidationError('No puede haber más golpes acertados que golpes totales.', code='invalid_kicks')