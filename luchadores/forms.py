from django import forms
from .models import Luchador


class LuchadorForm(forms.ModelForm):
    class Meta:
        model = Luchador
        fields = ['nombre', 'apellidos', 'peso', 'altura', 'alcance', 'empates', 'victorias', 'derrotas', 'nacimiento']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'altura': forms.NumberInput(attrs={'class': 'form-control'}),
            'alcance': forms.NumberInput(attrs={'class': 'form-control'}),
            'empates': forms.NumberInput(attrs={'class': 'form-control'}),
            'victorias': forms.NumberInput(attrs={'class': 'form-control'}),
            'derrotas': forms.NumberInput(attrs={'class': 'form-control'}),
            'nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
        }