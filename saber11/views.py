from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .serializers import ColegioSerializer
from rest_framework import generics

from .models import Colegio

def index(request):
    cols = Colegio.objects.filter(promponderado__gt=68).order_by('-promponderado')
    context = {'colegios': cols}
    return render(request, 'saber11/index.html', context)


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
    queryset = Colegio.objects.filter(promponderado__gt=65)
    queryset = queryset.exclude(evaluados__lte=5).order_by('-promponderado')
    template_name = 'saber11/detalle.html'


class ColegioList(generics.ListAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer


class ColegioDetail(generics.RetrieveAPIView):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer
