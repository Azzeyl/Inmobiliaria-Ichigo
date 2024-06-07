from django import forms
from inmobiliaria_app.models import Inmobiliaria,Propietario,Edificio,Casa,Finca

class InmobiliariaForm(forms.ModelForm):
    class Meta:
        model = Inmobiliaria
        fields = ['nombre','direccion','telefono']

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre','cedula','inmobiliaria']

class EdificioForm(forms.ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre','direccion','numero_pisos','numero_apartamentos','numero_habitaciones','inmobiliaria','propietarios']

class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ['localidad','direccion','numero_habitaciones','area_terreno','inmobiliaria','propietarios']

class FincaForm(forms.ModelForm):
    class Meta:
        model = Finca
        fields = ['nombre','direccion','area_total','tipo_terreno','inmobiliaria','propietarios']

