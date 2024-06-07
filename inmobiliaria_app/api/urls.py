from django.urls import path
from inmobiliaria_app.api.views import InmobiliariaListView,InmobiliariaCreateView,PropietarioListView,PropietarioCreateView,EdificioListView,EdificioCreateView,CasaListView,CasaCreateView,FincaListView,FincaCreateView,InmobiliariaDeleteView,PropietarioDeleteView,EdificioDeleteView,CasaDeleteView,FincaDeleteView,InmobiliariaUpdateView,PropietarioUpdateView,IndexView,EdificioUpdateView,CasaUpdateView,FincaUpdateView

urlpatterns = [
    path('inmobiliariaHome/', IndexView.as_view(), name='index-view'),
    path('inmobiliaria/', InmobiliariaListView.as_view(), name='inmobiliaria-list'),
    path('inmobiliaria/crear/', InmobiliariaCreateView.as_view(), name='inmobiliaria-create'),
    path('inmobiliaria/eliminar/<int:pk>/', InmobiliariaDeleteView.as_view(), name='inmobiliaria-delete'),
    path('inmobiliaria/actualizar/<int:pk>/', InmobiliariaUpdateView.as_view(), name='inmobiliaria-update'),


    path('propietario/', PropietarioListView.as_view(), name='propietario-list'),
    path('propietario/crear/', PropietarioCreateView.as_view(), name='propietario-create'),
    path('propietario/eliminar/<int:pk>/', PropietarioDeleteView.as_view(), name='propietario-delete'),
    path('propietario/actualizar/<int:pk>/', PropietarioUpdateView.as_view(), name='propietario-update'),
    

    path('edificio/', EdificioListView.as_view(), name='edificio-list'),
    path('edificio/crear/', EdificioCreateView.as_view(), name='edificio-create'),
    path('edificio/eliminar/<int:pk>/', EdificioDeleteView.as_view(), name='edificio-delete'),
    path('edificio/actualizar/<int:pk>/', EdificioUpdateView.as_view(), name='edificio-update'),


    path('casa/', CasaListView.as_view(), name='casa-list'),
    path('casa/crear/', CasaCreateView.as_view(), name='casa-create'),
    path('casa/eliminar/<int:pk>/', CasaDeleteView.as_view(), name='casa-delete'),
    path('casa/actualizar/<int:pk>/', CasaUpdateView.as_view(), name='casa-update'),

    

    path('finca/', FincaListView.as_view(), name='finca-list'),
    path('finca/crear/', FincaCreateView.as_view(), name='finca-create'),
    path('finca/eliminar/<int:pk>/', FincaDeleteView.as_view(), name='finca-delete'),
    path('finca/actualizar/<int:pk>/', FincaUpdateView.as_view(), name='finca-update'),
]