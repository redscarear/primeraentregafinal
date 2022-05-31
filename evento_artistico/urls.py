from django.urls import path

from evento_artistico import views
from evento_artistico import forms

urlpatterns = [
    path('', views.index, name='Home'),
    path('Productores', views.productores, name='productores'),
    path('productores_form', views.productor_form, name='productoresform'),
    path('musicos', views.musicos, name='musicos'),
    path('musicos_form', views.musicos_form, name='musicosform' ),
    path('tecnicos', views.tecnicos, name='tecnicos'),
    path('tecnicos_form', views.tecnicos_form, name='tecnicosform'),
    path('search', views.search, name='search'),

]