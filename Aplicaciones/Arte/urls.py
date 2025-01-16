from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_view, name='login'),
    path('home1/', views.home1, name='home1'),
<<<<<<< HEAD
 # Artista
    path('listadoArtistas/', views.listadoArtistas, name='listado_artistas'),
    path('eliminarArtista/<int:id>/', views.eliminarArtista, name='eliminar_artista'),
    path('editarArtista/<int:id>/', views.editarArtista, name='editar_artista'),
    path('guardarArtista/', views.guardarArtista, name='guardar_artista'),
    path('procesoActualizarArtista/', views.procesoActualizarArtista, name='proceso_actualizar_artista'),
    path('nuevoArtista/', views.nuevoArtista, name='nuevo_artista'),
    # Ubicacion
    path('listadoUbicaciones/', views.listadoUbicaciones, name='listado_ubicaciones'),
    path('eliminarUbicacion/<int:id>/', views.eliminarUbicacion, name='eliminar_ubicacion'),
    path('editarUbicacion/<int:id>/', views.editarUbicacion, name='editar_ubicacion'),
    path('guardarUbicacion/', views.guardarUbicacion, name='guardar_ubicacion'),
    path('procesoActualizarUbicacion/', views.procesoActualizarUbicacion, name='proceso_actualizar_ubicacion'),
    path('nuevaUbicacion/', views.nuevaUbicacion, name='nueva_ubicacion'),
    # Organizador
    path('listadoOrganizadores/', views.listadoOrganizadores, name='listado_organizadores'),
    path('eliminarOrganizador/<int:id>/', views.eliminarOrganizador, name='eliminar_organizador'),
    path('editarOrganizador/<int:id>/', views.editarOrganizador, name='editar_organizador'),
    path('guardarOrganizador/', views.guardarOrganizador, name='guardar_organizador'),
    path('procesoActualizarOrganizador/', views.procesoActualizarOrganizador, name='proceso_actualizar_organizador'),
    path('nuevoOrganizador/', views.nuevoOrganizador, name='nuevo_organizador'),
    # Evento
    path('listadoEventos/', views.listadoEventos, name='listado_eventos'),
    path('eliminarEvento/<int:id>/', views.eliminarEvento, name='eliminar_evento'),
    path('editarEvento/<int:id>/', views.editarEvento, name='editar_evento'),
    path('guardarEvento/', views.guardarEvento, name='guardar_evento'),
    path('procesoActualizarEvento/', views.procesoActualizarEvento, name='proceso_actualizar_evento'),
    path('nuevoEvento/', views.nuevoEvento, name='nuevo_evento'),
    # PublicacionEvento
    path('listadoPublicacionesEvento/', views.listadoPublicacionesEvento, name='listado_publicaciones_evento'),
    path('eliminarPublicacionEvento/<int:id>/', views.eliminarPublicacionEvento, name='eliminar_publicacion_evento'),
    path('editarPublicacionEvento/<int:id>/', views.editarPublicacionEvento, name='editar_publicacion_evento'),
    path('guardarPublicacionEvento/', views.guardarPublicacionEvento, name='guardar_publicacion_evento'),
    path('procesoActualizarPublicacionEvento/', views.procesoActualizarPublicacionEvento, name='proceso_actualizar_publicacion_evento'),
    path('nuevaPublicacionEvento/', views.nuevaPublicacionEvento, name='nueva_publicacion_evento'),
=======

>>>>>>> 8f99e044b8648af0827d61f17605141454ca18b1
]
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
