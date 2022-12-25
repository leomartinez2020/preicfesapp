from django.urls import path

from . import views

app_name = 'icfesapp'
urlpatterns = [
    path('indice/', views.main, name='main'),
    path('<slug:slug>/<int:pk>/', views.prueba, name='prueba'),
    path('<int:quiz_id>/resultados/', views.revisar, name='revisar'),
]
