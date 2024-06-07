from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from inmobiliaria_app.admin import Inmobiliaria,Propietario,Edificio,Casa,Finca
from inmobiliaria_app.api.serializers import InmobiliariaSerializer,PropietarioSerializer,EdificioSerializer,CasaSerializer,FincaSerializer

from rest_framework.views import APIView
from rest_framework import status
from inmobiliaria_app.models import Inmobiliaria, Propietario, Edificio, Casa, Finca
from inmobiliaria_app.api.forms import InmobiliariaForm,PropietarioForm,EdificioForm,CasaForm,FincaForm
from django.shortcuts import render, redirect, get_object_or_404


#clase Home

class IndexView(APIView):
    def get(self, request):
        return render(request, 'index.html')

# Clase inmobiliaria

class InmobiliariaListView(APIView):
    def get(self, request):
        inmobiliaria = Inmobiliaria.objects.all()
        serializer = InmobiliariaSerializer(inmobiliaria, many=True)
        return render(request, 'inmobiliaria.html', {'inmobiliaria':serializer.data})

class InmobiliariaCreateView(APIView):
    def get(self, request):
        form = InmobiliariaForm()
        return render(request, 'crear_inmobiliaria.html', {'form': form})
    def post(self, request):
        form = InmobiliariaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/inmobiliaria/')
        return render(request, 'crear_inmobiliaria.html', {'form': form})
    
class InmobiliariaDeleteView(APIView):
    def delete(self, request, pk):
        try:
            inmobiliaria = Inmobiliaria.objects.get(pk=pk)
            inmobiliaria.delete()
            return HttpResponseRedirect('/portal/inmobiliaria/')
        except Inmobiliaria.DoesNotExist:
            return render(request, 'inmobiliaria.html', {'error_message': 'La inmobiliaria no existe.'})

class InmobiliariaUpdateView(APIView):
    def get(self, request, pk):
        inmobiliaria = Inmobiliaria.objects.get(pk=pk)
        form = InmobiliariaForm(instance=inmobiliaria)
        return render(request, 'actualizar_inmobiliaria.html', {'form': form, 'inmobiliaria': inmobiliaria})

    def put(self, request, pk):
        inmobiliaria = Inmobiliaria.objects.get(pk=pk)
        form = InmobiliariaForm(request.POST, instance=inmobiliaria)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/inmobiliaria/')
        return render(request, 'actualizar_inmobiliaria.html', {'form': form, 'inmobiliaria': inmobiliaria})

    def post(self, request, pk):
        inmobiliaria = Inmobiliaria.objects.get(pk=pk)
        form = InmobiliariaForm(request.POST, instance=inmobiliaria)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/inmobiliaria/')
        return render(request, 'actualizar_inmobiliaria.html', {'form': form, 'inmobiliaria': inmobiliaria})


#clase Propietario

class PropietarioListView(APIView):
    def get(self, request):
        propietario = Propietario.objects.all()
        serializer = PropietarioSerializer(propietario, many=True)
        return render(request, 'propietario.html', {'propietario':serializer.data})

class PropietarioCreateView(APIView):
    def get(self, request):
        form = PropietarioForm()
        return render(request, 'crear_propietario.html', {'form': form})
    def post(self, request):
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/propietario/')
        return render(request, 'crear_propietario.html', {'form': form})
    
class PropietarioDeleteView(APIView):
    def delete(self, request, pk):
        try:
            propietario = Propietario.objects.get(pk=pk)
            propietario.delete()
            return HttpResponseRedirect('/portal/propietario/')
        except Propietario.DoesNotExist:
            return render(request, 'propietario.html', {'error_message': 'El propietario no existe.'})

class PropietarioUpdateView(APIView):
    def get(self, request, pk):
        propietario = Propietario.objects.get(pk=pk)
        form = PropietarioForm(instance=propietario)
        return render(request, 'actualizar_propietario.html', {'form': form, 'propietario': propietario})

    def put(self, request, pk):
        propietario = Propietario.objects.get(pk=pk)
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/propietario/')
        return render(request, 'actualizar_propietario.html', {'form': form, 'propietario': propietario})

    def post(self, request, pk):
        propietario = Propietario.objects.get(pk=pk)
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/propietario/')
        return render(request, 'actualizar_propietario.html', {'form': form, 'propietario': propietario})

#clase Edificio

class EdificioListView(APIView):
    def get(self, request):
        edificio = Edificio.objects.all()
        serializer = EdificioSerializer(edificio, many=True)
        return render(request, 'edificio.html', {'edificio':serializer.data})

class EdificioCreateView(APIView):
    def get(self, request):
        form = EdificioForm()
        return render(request, 'crear_edificio.html', {'form': form})
    def post(self, request):
        form = EdificioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/edificio/')
        return render(request, 'crear_edificio.html', {'form': form})
    
class EdificioDeleteView(APIView):
    def delete(self, request, pk):
        try:
            edificio = Edificio.objects.get(pk=pk)
            edificio.delete()
            return HttpResponseRedirect('/portal/inmobiliaria/')
        except Edificio.DoesNotExist:
            return render(request, 'edificio.html', {'error_message': 'El edificio no existe.'})
        
class EdificioUpdateView(APIView):
    def get(self, request, pk):
        edificio = Edificio.objects.get(pk=pk)
        form = EdificioForm(instance=edificio)
        return render(request, 'actualizar_edificio.html', {'form': form, 'edificio': edificio})

    def put(self, request, pk):
        edificio = Edificio.objects.get(pk=pk)
        form = EdificioForm(request.POST, instance=edificio)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/edificio/')
        return render(request, 'actualizar_edificio.html', {'form': form, 'edificio': edificio})

    def post(self, request, pk):
        edificio = Edificio.objects.get(pk=pk)
        form = EdificioForm(request.POST, instance=edificio)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/edificio/')
        return render(request, 'actualizar_edificio.html', {'form': form, 'edificio': edificio})

#Clase Casa

class CasaListView(APIView):
    def get(self, request):
        casa = Casa.objects.all()
        serializer = CasaSerializer(casa, many=True)
        return render(request, 'casa.html', {'casa':serializer.data})

class CasaCreateView(APIView):
    def get(self, request):
        form = CasaForm()
        return render(request, 'crear_casa.html', {'form': form})
    def post(self, request):
        form = CasaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/casa/')
        return render(request, 'crear_casa.html', {'form': form})

class CasaDeleteView(APIView):
    def delete(self, request, pk):
        try:
            casa = Casa.objects.get(pk=pk)
            casa.delete()
            return HttpResponseRedirect('/portal/inmobiliaria/')
        except Casa.DoesNotExist:
            return render(request, 'casa.html', {'error_message': 'La casa no existe.'})
        
class CasaUpdateView(APIView):
    def get(self, request, pk):
        casa = Casa.objects.get(pk=pk)
        form = CasaForm(instance=casa)
        return render(request, 'actualizar_casa.html', {'form': form, 'casa': casa})

    def put(self, request, pk):
        casa = Casa.objects.get(pk=pk)
        form = CasaForm(request.POST, instance=casa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/casa/')
        return render(request, 'actualizar_casa.html', {'form': form, 'casa': casa})

    def post(self, request, pk):
        casa = Casa.objects.get(pk=pk)
        form = EdificioForm(request.POST, instance=casa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/casa/')
        return render(request, 'actualizar_casa.html', {'form': form, 'casa': casa})

#Clase Finca

class FincaListView(APIView):
    def get(self, request):
        finca = Finca.objects.all()
        serializer = FincaSerializer(finca, many=True)
        return render(request, 'finca.html', {'finca':serializer.data})

class FincaCreateView(APIView):
    def get(self, request):
        form = FincaForm()
        return render(request, 'crear_finca.html', {'form': form})
    def post(self, request):
        form = FincaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/finca/')
        return render(request, 'crear_finca.html', {'form': form})
    
class FincaDeleteView(APIView):
    def delete(self, request, pk):
        try:
            finca = Finca.objects.get(pk=pk)
            finca.delete()
            return HttpResponseRedirect('/portal/finca/')
        except Finca.DoesNotExist:
            return render(request, 'finca.html', {'error_message': 'La finca no existe.'})
        
class FincaUpdateView(APIView):
    def get(self, request, pk):
        finca = Finca.objects.get(pk=pk)
        form = FincaForm(instance=finca)
        return render(request, 'actualizar_finca.html', {'form': form, 'finca': finca})

    def put(self, request, pk):
        finca = Finca.objects.get(pk=pk)
        form = CasaForm(request.POST, instance=finca)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/finca/')
        return render(request, 'actualizar_finca.html', {'form': form, 'finca': finca})

    def post(self, request, pk):
        finca = Finca.objects.get(pk=pk)
        form = FincaForm(request.POST, instance=finca)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/portal/finca/')
        return render(request, 'actualizar_finca.html', {'form': form, 'finca': finca})

