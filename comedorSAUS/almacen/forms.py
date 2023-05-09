from django import forms
from .models import Insumo


class FormInsumo(forms.ModelForm):

    class Meta:
        model = Insumo
        fields = '__all__'

class FormInsumoEditar(FormInsumo):
    class Meta:
        exclude = ['id']
        model = Insumo

class FiltrosInsumo(FormInsumo):
    def __init__(self, *args, **kwargs):
        super(FiltrosInsumo, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False