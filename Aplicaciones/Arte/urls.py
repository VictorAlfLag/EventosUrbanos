from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home1/', views.home1, name='home1'),
    

    # Listings (Listar)
    path('artists/', views.list_artists, name='list_artists'),
    path('licencias/', views.list_licenses, name='list_licenses'),
    path('auditorias/', views.list_audits, name='list_audits'),
    path('locations/', views.list_locations, name='list_locations'),
    path('organizers/', views.list_organizers, name='list_organizers'),
    path('events/', views.list_events, name='list_events'),
    path('publications/', views.list_event_publications, name='list_event_publications'),

    # New (Nuevo)
    path('new/artist/', views.new_artist, name='new_artist'),
    path('licencia/nueva/', views.new_license, name='new_license'),
    path('auditoria/nueva/', views.new_audit, name='new_audit'),
    path('new/location/', views.new_location, name='new_location'),
    path('new/organizer/', views.new_organizer, name='new_organizer'),
    path('new/event/', views.new_event, name='new_event'),
    path('new/publication/', views.new_event_publication, name='new_event_publication'),

    # Save (Guardar)
    path('save/artist/', views.save_artist, name='save_artist'),
    path('auditoria/guardar/', views.save_audit, name='save_audit'),
    path('licencia/guardar/', views.save_license, name='save_license'),
    path('save/location/', views.save_location, name='save_location'),
    path('save/organizer/', views.save_organizer, name='save_organizer'),
    path('save/event/', views.save_event, name='save_event'),
    path('save/publication/', views.save_event_publication, name='save_event_publication'),

    # Edit (Editar)
    path('edit/artist/<int:id>/', views.edit_artist, name='edit_artist'),
    path('edit/location/<int:id>/', views.edit_location, name='edit_location'),
    path('licencia/editar/<int:id>/', views.edit_license, name='edit_license'),
    path('auditoria/editar/<int:id>/', views.edit_audit, name='edit_audit'),
    path('edit/organizer/<int:id>/', views.edit_organizer, name='edit_organizer'),
    path('edit/event/<int:id>/', views.edit_event, name='edit_event'),
    path('edit/publication/<int:id>/', views.edit_event_publication, name='edit_event_publication'),

    # Delete (Eliminar)
    path('delete/artist/<int:id>/', views.delete_artist, name='delete_artist'),
    path('delete/location/<int:id>/', views.delete_location, name='delete_location'),
    path('auditoria/eliminar/<int:id>/', views.delete_audit, name='delete_audit'),
    path('licencia/eliminar/<int:id>/', views.delete_license, name='delete_license'),
    path('delete/organizer/<int:id>/', views.delete_organizer, name='delete_organizer'),
    path('delete/event/<int:id>/', views.delete_event, name='delete_event'),
    path('delete/publication/<int:id>/', views.delete_event_publication, name='delete_event_publication'),


    path('update/artist/<int:id>/', views.update_artist, name='update_artist'),
    path('update/location/<int:id>/', views.update_location, name='update_location'),
    path('licencia/actualizar/<int:id>/', views.update_license, name='update_license'),
    path('update/organizer/<int:id>/', views.update_organizer, name='update_organizer'),
    path('auditoria/actualizar/<int:id>/', views.update_audit, name='update_audit'),
    path('update/event/<int:id>/', views.update_event, name='update_event')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
