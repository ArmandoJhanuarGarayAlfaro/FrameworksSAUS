from django import forms
from .models import TipoInsumo, Insumo


########################### TIPO INSUMO ###########################
class FormTipoInsumo(forms.ModelForm):

    class Meta:
        model = TipoInsumo
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Nombre'}
            ),
            'unidad_medida': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Unidad de medida'}
            ),
        }


class FormTipoIngredienteEditar(FormTipoInsumo):
    class Meta:
        exclude = ['id']
        model = TipoInsumo

        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Nombre'}
            ),
            'unidad_medida': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Unidad de medida'}
            ),
        }


class FiltrosTipoInsumo(FormTipoInsumo):
    def __init__(self, *args, **kwargs):
        super(FiltrosTipoInsumo, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False


########################### INSUMO ###########################
class FormInsumo(forms.ModelForm):

    class Meta:
        model = Insumo
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Nombre'}
            ),
            'codigo': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Código'}
            ),
            'cantidad': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Cantidad'}
            ),
            'numero_lote': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Número de Lote'}
            ),
            'fecha_caducidad': forms.DateInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Fecha de Caducidad'}
            ),
            'proveedor': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Proveedor'}
            ),
            'tipo': forms.Select(
                attrs={'class': 'form-control form-control-lg'}
            ),
        }


class FormInsumoEditar(FormTipoInsumo):
    class Meta:
        exclude = ['id']
        model = Insumo

        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Nombre'}
            ),
            'codigo': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Código'}
            ),
            'cantidad': forms.NumberInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Cantidad'}
            ),
            'numero_lote': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Número de lote'}
            ),
            'fecha_caducidad': forms.DateInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Fecha de caducidad'}
            ),
            'proveedor': forms.TextInput(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Proveedor'}
            ),
            'tipo': forms.Select(
                attrs={'class': 'form-control form-control-lg',
                       'placeholder': 'Tipo de insumo'}
            ),
        }


class FiltrosInsumo(FormInsumo):
    tipo = forms.ModelChoiceField(queryset=TipoInsumo.objects.all(), empty_label="Tipo de insumo", 
                                  required=False, widget=forms.Select(attrs={'class': 'form-control form-control-lg'}))

    def __init__(self, *args, **kwargs):
        super(FiltrosInsumo, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].required = False
