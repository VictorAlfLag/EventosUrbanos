from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_view, name='login'),
    path('home1/', views.home1, name='home1'),
 # Artista
    path('artistas/', views.listadoArtistas, name='listado_artistas'),
    path('artista/nuevo/', views.nuevoArtista, name='nuevo_artista'),
    path('artista/editar/<int:id>/', views.editarArtista, name='editar_artista'),
    path('artista/eliminar/<int:id>/', views.eliminarArtista, name='eliminar_artista'),
    
    # Ubicacion
    path('ubicaciones/', views.listadoUbicaciones, name='listado_ubicaciones'),
    path('ubicacion/nueva/', views.nuevaUbicacion, name='nueva_ubicacion'),
    path('ubicacion/editar/<int:id>/', views.editarUbicacion, name='editar_ubicacion'),
    path('ubicacion/eliminar/<int:id>/', views.eliminarUbicacion, name='eliminar_ubicacion'),
    
    # Organizador
    path('organizadores/', views.listadoOrganizadores, name='listado_organizadores'),
    path('organizador/nuevo/', views.nuevoOrganizador, name='nuevo_organizador'),
    path('organizador/editar/<int:id>/', views.editarOrganizador, name='editar_organizador'),
    path('organizador/eliminar/<int:id>/', views.eliminarOrganizador, name='eliminar_organizador'),
    
    # Evento
    path('eventos/', views.listadoEventos, name='listado_eventos'),
    path('evento/nuevo/', views.nuevoEvento, name='nuevo_evento'),
    path('evento/editar/<int:id>/', views.editarEvento, name='editar_evento'),
    path('evento/eliminar/<int:id>/', views.eliminarEvento, name='eliminar_evento'),
    
    # PublicacionEvento
    path('publicaciones/', views.listadoPublicaciones, name='listado_publicaciones'),
    path('publicacion/nueva/', views.nuevaPublicacion, name='nueva_publicacion'),
    path('publicacion/editar/<int:id>/', views.editarPublicacion, name='editar_publicacion'),
    path('publicacion/eliminar/<int:id>/', views.eliminarPublicacion, name='eliminar_publicacion'),
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
