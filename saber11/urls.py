from django.urls import path

from . import views

app_name = 'saber11'
urlpatterns = [
    path('search/', views.search, name='search'),
    path('indice/', views.ColegioListView.as_view(), name='index'),
    path('detalle/<slug:slug>/<int:pk>/', views.ColegioDetailView.as_view(), name='detalle'),
    path('cols/', views.ColegioList.as_view()),
    path('cols/<int:pk>/', views.ColegioDetail.as_view()),
    path('depts/', views.DepartamentoList.as_view()),
    path('depts/<int:pk>/', views.DepartamentoDetail.as_view()),
]
