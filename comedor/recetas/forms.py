from django import forms
from .models import Receta


class FormReceta(forms.ModelForm):

    class Meta:
        model = Receta
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Nombre'}
            ),
            'descripcion': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Descripcion corta de receta'}
            ), 
            'hora': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Tiempo de hora que tarda la receta'}
            ),
            'minuto': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Tiempo de minutos que tarda la receta'}
            ),
            'ingredientes': forms.Textarea(
                attrs={'class': 'form-control form-control-lg textarea.form-control-lg',
                       'placeholder': 'Listado de ingredientes y porciones'}
            ),
            'instrucciones': forms.Textarea(
                attrs={'class': 'form-control form-control-lg textarea.form-control-lg',
                       'placeholder': 'Pasos a seguir para hacer la receta'}
            ),
        }

class FormRecetaEditar(FormReceta):
    class Meta:
        exclude = ['id']
        model = Receta

        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Nombre'}
            ),
            'descripcion': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Descripcion corta de receta'}
            ), 
            'hora': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Tiempo de hora que tarda la receta'}
            ),
            'minuto': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Tiempo de minutos que tarda la receta'}
            ),
            'ingredientes': forms.Textarea(
                attrs={'class': 'form-control form-control-lg textarea',
                       'placeholder': 'Listado de ingredientes y porciones'}
            ),
            'instrucciones': forms.Textarea(
                attrs={'class': 'form-control form-control-lg textarea',
                       'placeholder': 'Pasos a seguir para hacer la receta'}
            ),
        }

class FiltrosReceta(FormReceta):
    def __init__(self, *args, **kwargs):
        super(FiltrosReceta, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False