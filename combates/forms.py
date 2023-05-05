from django import forms
from .models import Combate
from luchadores.models import Luchador

class CombateForm(forms.ModelForm):
    fecha = forms.DateField(widget=forms.SelectDateWidget(
        attrs={'class': 'form-control datepicker_input'}, years=[y for y in range(1950,2023)]))
    class Meta:
        model = Combate
        fields = ['luchador_rojo', 'luchador_azul', 'fecha', 'round_max', 'resultado', 
                    'golpes_rojo', 'golpes_acertados_rojo',
                    'golpes_azul', 'golpes_acertados_azul']
        
        widgets = {
            'luchador_rojo': forms.Select(attrs={'class': 'form-control'}),
            'luchador_azul': forms.Select(attrs={'class': 'form-control'}),
            'round_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'resultado': forms.Select(attrs={'class': 'form-control'}),
            'golpes_rojo': forms.NumberInput(attrs={'class': 'form-control'}),
            'golpes_acertados_rojo': forms.NumberInput(attrs={'class': 'form-control'}),
            'golpes_azul': forms.NumberInput(attrs={'class': 'form-control'}),
            'golpes_acertados_azul': forms.NumberInput(attrs={'class': 'form-control'}),
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