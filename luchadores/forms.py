from django import forms
from .models import Luchador

DATE_INPUT_FORMATS = ["%d.%m.%Y"]


class LuchadorForm(forms.ModelForm):
    nacimiento = forms.DateField(widget=forms.SelectDateWidget(
        attrs={'class': 'form-control datepicker_input'}, years=[y for y in range(1950,2023)], ))
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
            'nacimiento': forms.DateInput(attrs={'class': 'form-control datepicker_input'}),
        }
        
class LuchadorEditForm(forms.ModelForm):
    nacimiento = forms.DateField(widget=forms.SelectDateWidget(
        attrs={'class': 'form-control datepicker_input'}, years=[y for y in range(1950,2023)]))
    class Meta:
        model = Luchador
        fields = ['nombre', 'apellidos', 'peso', 'altura', 'alcance', 'nacimiento']
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