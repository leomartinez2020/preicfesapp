#from django.conf import settings
#from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'preicfesapp'
urlpatterns = [
    path('', TemplateView.as_view(template_name='preicfesapp/index.html'), name='inicio'),
    path('indice/', views.main, name='main'),
    path('<int:pk>/', views.prueba, name='prueba'),
    path('<int:quiz_id>/resultados/', views.revisar, name='revisar'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
