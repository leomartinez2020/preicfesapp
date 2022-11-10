from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'preicfesapp'
urlpatterns = [
    path('', TemplateView.as_view(template_name='preicfesapp/index.html')),
    path('indice/', views.index, name='index'),
    path('<str:categoria>/', views.prueba, name='prueba'),
    path('<int:quiz_id>/resultados/', views.revisar, name='revisar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
