import logging

from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .serializers import ColegioSerializer, DepartamentoSerializer
from rest_framework import generics

from .models import Colegio, Municipio, Departamento
from .forms import MunicipioForm, DepartamentoForm

#logging.basicConfig(filename='saber.log', encoding='utf-8', level=logging.DEBUG)

def search(request):
    #cols = Colegio.objects.filter(promponderado__gt=68).order_by('-promponderado')
    #neiva = Municipio.objects.get(pk=23)
    #logging.info('processing request')
    form2 = DepartamentoForm()
    if request.method == 'GET' and request.GET.get('municipio'):
        municipio = request.GET['municipio']
        #municipio = request.GET.get('municipio')
        departamento = request.GET['departamento']
        query = Colegio.objects.filter(ubicacion__nombre=municipio).order_by('-promponderado')
        colegios = query.exclude(puntajeglobal__isnull=True)
        logging.info(municipio)
        logging.info(f'Colegios en {municipio}: {colegios.count()}')
        context = {'form2': form2, 'colegios': colegios, 'municipio': municipio, 'departamento': departamento}
        return render(request, 'saber11/search.html', context)
    #data = {'nombre': 'Neiva', 'departamento': 'Huila'}
    #form = MunicipioForm()
    #context = {'form': form, 'form2': form2}
    context = {'form2': form2}
    return render(request, 'saber11/search.html', context)


class ColegioListView(ListView):
    model = Colegio
    paginate_by = 10
    context_object_name = 'colegios'
    queryset = Colegio.objects.filter(promponderado__gt=65)
    queryset = queryset.exclude(evaluados__lte=5).order_by('-promponderado')[:100]
    template_name = 'saber11/index.html'


class ColegioDetailView(DetailView):
    context_object_name = 'colegio'
    model = Colegio
    #queryset = Colegio.objects.filter(promponderado__gt=65)
    #queryset = queryset.exclude(evaluados__lte=5).order_by('-promponderado')
    queryset = Colegio.objects.filter(promponderado__gt=25).order_by('-promponderado')
    template_name = 'saber11/detalle.html'


class ColegioList(generics.ListAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer


class ColegioDetail(generics.RetrieveAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer


class DepartamentoList(generics.ListAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class DepartamentoDetail(generics.RetrieveAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
