from django.urls import path

from . import views

app_name = 'saber11'
urlpatterns = [
    #path('indice/', views.index, name='index'),
    path('indice/', views.ColegioListView.as_view(), name='index'),
    path('detalle/<int:pk>/', views.ColegioDetailView.as_view(), name='detalle'),
    path('cols/', views.ColegioList.as_view()),
    path('cols/<int:pk>/', views.ColegioDetail.as_view()),
]
