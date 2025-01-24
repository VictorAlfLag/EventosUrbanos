from .models import Artist, Location, Organizer, Event, EventPublication, License, Audit
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'home.html')
def home1(request):
    return render(request, 'home1.html')
# <----------List---------->
def list_artists(request):
    artists = Artist.objects.all()
    return render(request, "ARTISTA/listadoArtistas.html", {'artist_list': artists})

def list_locations(request):
    locations = Location.objects.all()
    return render(request, "UBICACION/listadoUbicacion.html", {'location_list': locations})

def list_organizers(request):
    organizers = Organizer.objects.all()
    return render(request, "ORGANIZADOR/listadoOrganizador.html", {'organizer_list': organizers})

def list_events(request):
    events = Event.objects.select_related('artist', 'organizer', 'location').all()
    return render(request, "EVENTO/listadoEventos.html", {'event_list': events})

def list_event_publications(request):
    publications = EventPublication.objects.all()
    return render(request, "PUBLICACION/listadoPublicacion.html", {'publication_list': publications})
def new_artist(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        social_media = request.POST.get('social_media')
        website = request.POST.get('website')

        artist = Artist.objects.create(
            name=name,
            description=description,
            phone=phone,
            email=email,
            social_media=social_media,
            website=website
        )
        return redirect('list_artists')
    return render(request, 'ARTISTA/nuevoArtista.html')


def new_location(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        description = request.POST.get('description')

        location = Location.objects.create(
            name=name,
            address=address,
            description=description
        )
        return redirect('list_locations')
    return render(request, 'UBICACION/nuevaUbicacion.html')


def new_organizer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        entity = request.POST.get('entity')
        description = request.POST.get('description')
        contact = request.POST.get('contact')
        contact_email = request.POST.get('contact_email')
        website = request.POST.get('website')

        organizer = Organizer.objects.create(
            name=name,
            entity=entity,
            description=description,
            contact=contact,
            contact_email=contact_email,
            website=website
        )
        return redirect('list_organizers')
    return render(request, 'ORGANIZADOR/nuevoOrganizador.html')


def new_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        status = request.POST.get('status')
        artist_id = request.POST.get('artist')
        organizer_id = request.POST.get('organizer')
        location_id = request.POST.get('location')
        artist = get_object_or_404(Artist, id=artist_id)
        organizer = get_object_or_404(Organizer, id=organizer_id)
        location = get_object_or_404(Location, id=location_id)
        event = Event.objects.create(
            ARTIST=artist,
            ORGANIZER=organizer,
            LOCATION=location,
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            status=status
        )
        
        return redirect('list_events')
    artists = Artist.objects.all()
    organizers = Organizer.objects.all()
    locations = Location.objects.all()
    return render(request, 'EVENTO/nuevoEvento.html', {
        'artists': artists,
        'organizers': organizers,
        'locations': locations,
    })

def new_event_publication(request):
    if request.method == 'POST':
        # Obtener el evento y la ubicación desde los datos del formulario
        event = get_object_or_404(Event, id=request.POST.get('event'))
        event_location = get_object_or_404(Location, id=request.POST.get('event_location'))

        # Obtener los otros datos
        event_time = request.POST.get('event_time')
        public_content = request.POST.get('public_content')
        event_image = request.FILES.get('event_image')
        publication_status = request.POST.get('publication_status')

        # Crear la publicación de evento con las claves foráneas
        publication = EventPublication.objects.create(
            event=event,
            event_time=event_time,
            public_content=public_content,
            event_image=event_image,
            publication_status=publication_status,
            event_location=event_location
        )

        # Asignar los artistas seleccionados si los hay
        selected_artists = request.POST.getlist('presented_artists')
        if selected_artists:
            artists = Artist.objects.filter(id__in=selected_artists)
            publication.presented_artists.set(artists)  # Relaciona los artistas con la publicación

        return redirect('list_event_publications')

    # Si es una solicitud GET, obtenemos todos los objetos necesarios para renderizar el formulario
    artists = Artist.objects.all()
    locations = Location.objects.all()
    events = Event.objects.all()

    return render(request, 'PUBLICACION/nuevaPublicacion.html', {
        'artists': artists,
        'locations': locations,
        'events': events,
    })



# <--------------Save--------------->
def save_artist(request):
    if request.method == 'POST':
        # Cambiar los nombres de los campos para que coincidan con el HTML
        name = request.POST.get('nombre')
        description = request.POST.get('descripcion')
        phone = request.POST.get('telefono')
        email = request.POST.get('email')
        social_media = request.POST.get('redes_sociales')
        website = request.POST.get('sitio_web')
        
        # Crear el artista
        artist = Artist.objects.create(
            name=name,
            description=description,
            phone=phone,
            email=email,
            social_media=social_media,
            website=website
        )
        
        # Mensaje de éxito y redirección
        messages.success(request, "Artist successfully registered.")
        return redirect('list_artists')
    
    return redirect('artist_form')


def save_location(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        description = request.POST['description']

        Location.objects.create(
            name=name,
            address=address,
            description=description
        )

        messages.success(request, "Location successfully registered.")
        return redirect('list_locations')
    return redirect('location_form')

def save_organizer(request):
    if request.method == 'POST':
        name = request.POST['name']
        entity = request.POST['entity']
        description = request.POST['description']
        contact = request.POST.get('contact', '')
        contact_email = request.POST.get('contact_email', '')
        website = request.POST.get('website', '')

        Organizer.objects.create(
            name=name,
            entity=entity,
            description=description,
            contact=contact,
            contact_email=contact_email,
            website=website
        )

        messages.success(request, "Organizer successfully registered.")
        return redirect('list_organizers')
    return redirect('organizer_form')

def save_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        status = request.POST.get('status')
        artist_id = request.POST.get('artist')
        organizer_id = request.POST.get('organizer')
        location_id = request.POST.get('location')

        # Obtener los objetos relacionados utilizando get_object_or_404
        artist = get_object_or_404(Artist, id=artist_id)
        organizer = get_object_or_404(Organizer, id=organizer_id)
        location = get_object_or_404(Location, id=location_id)

        # Crear el evento utilizando los nombres de los campos en minúsculas
        event = Event.objects.create(
            artist=artist,  # Usar 'artist' en minúsculas
            organizer=organizer,  # Usar 'organizer' en minúsculas
            location=location,  # Usar 'location' en minúsculas
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date,
            status=status
        )

        return redirect('list_events')

    artists = Artist.objects.all()
    organizers = Organizer.objects.all()
    locations = Location.objects.all()

    return render(request, 'EVENTO/nuevoEvento.html', {
        'artists': artists,
        'organizers': organizers,
        'locations': locations
    })


def save_event_publication(request):
    if request.method == 'POST':
        event_id = request.POST['event']
        public_content = request.POST['public_content']
        event_time = request.POST['event_time']
        publication_status = request.POST.get('publication_status', 'active')
        presented_artists_ids = request.POST.getlist('presented_artists')
        location_id = request.POST['event_location']
        event_image = request.FILES.get('event_image', None)

        event = get_object_or_404(Event, id=event_id)
        location = get_object_or_404(Location, id=location_id)

        publication = EventPublication.objects.create(
            event=event,
            public_content=public_content,
            event_time=event_time,
            publication_status=publication_status,
            event_location=location,
            event_image=event_image
        )

        publication.presented_artists.set(presented_artists_ids)

        messages.success(request, "Event publication successfully registered.")
        return redirect('list_event_publications')
    return redirect('event_publication_form')

# <----------Edit---------->
def edit_artist(request, id):
    artist = get_object_or_404(Artist, id=id)
    
    if request.method == 'POST':
        artist.name = request.POST.get('name')
        artist.description = request.POST.get('description')
        artist.phone = request.POST.get('phone')
        artist.email = request.POST.get('email')
        artist.social_media = request.POST.get('social_media')
        artist.website = request.POST.get('website')
        
        artist.save()
        return redirect('list_artists')
    
    return render(request, 'ARTISTA/editarArtista.html', {'artist': artist})

def edit_location(request, id):
    location = get_object_or_404(Location, id=id)
    if request.method == 'POST':
        location.name = request.POST.get('name')
        location.address = request.POST.get('address')
        location.description = request.POST.get('description')
        location.save()
        return redirect('list_locations')
    return render(request, 'Ubicacion/editarUbicacion.html', {'location': location})

def edit_organizer(request, id):
    organizer = get_object_or_404(Organizer, id=id)
    if request.method == 'POST':
        organizer.name = request.POST.get('name')
        organizer.entity = request.POST.get('entity')
        organizer.description = request.POST.get('description')
        organizer.contact = request.POST.get('contact')
        organizer.contact_email = request.POST.get('contact_email')
        organizer.website = request.POST.get('website')
        organizer.save()
        return redirect('list_organizers')
    return render(request, 'ORGANIZADOR/editarOrganizador.html', {'organizer': organizer})

def edit_event(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == 'POST':
        # Obtener los datos del formulario
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.start_date = request.POST.get('start_date')
        event.end_date = request.POST.get('end_date')
        event.status = request.POST.get('status')
        
        # Asignar las claves foráneas correctamente
        artist_id = request.POST.get('artist')
        organizer_id = request.POST.get('organizer')
        location_id = request.POST.get('location')
        
        # Verificar si los IDs no son nulos y asignar las instancias correspondientes
        if artist_id:
            event.ARTIST = Artist.objects.get(id=artist_id)
        if organizer_id:
            event.ORGANIZER = Organizer.objects.get(id=organizer_id)
        if location_id:
            event.LOCATION = Location.objects.get(id=location_id)
        
        # Guardar el evento actualizado
        event.save()
        
        return redirect('list_events')

    # Obtener todos los objetos de los modelos relacionados
    artists = Artist.objects.all()
    organizers = Organizer.objects.all()
    locations = Location.objects.all()
    
    return render(request, 'EVENTO/editarEvento.html', {'event': event, 'artists': artists, 'organizers': organizers, 'locations': locations})

def edit_event_publication(request, id):
    publication = get_object_or_404(EventPublication, id=id)
    if request.method == 'POST':
        publication.public_content = request.POST.get('public_content')
        publication.publication_status = request.POST.get('publication_status')
        publication.event_time = request.POST.get('event_time')
        publication.event_image = request.FILES.get('event_image') if 'event_image' in request.FILES else publication.event_image
        publication.event_id = request.POST.get('event')
        publication.event_location_id = request.POST.get('event_location')
        publication.save()
        artists = request.POST.getlist('presented_artists')
        publication.presented_artists.set(artists)
        return redirect('list_event_publications')
    events = Event.objects.all()
    locations = Location.objects.all()
    artists = Artist.objects.all()
    return render(request, 'PUBLICACION/editarPublicacion.html', {'publication': publication, 'events': events, 'locations': locations, 'artists': artists})

# <-------------Update-------->
def update_artist(request, id):
    # Obtener el artista usando el id desde la URL
    try:
        artist = Artist.objects.get(id=id)
    except Artist.DoesNotExist:
        messages.error(request, "Artist not found.")
        return redirect('list_artists')
    
    if request.method == 'POST':
        # Obtener los nuevos datos del formulario
        artist.name = request.POST.get('name')
        artist.description = request.POST.get('description')
        artist.phone = request.POST.get('phone')
        artist.email = request.POST.get('email')
        artist.social_media = request.POST.get('social_media')
        artist.website = request.POST.get('website')
        
        artist.save()
        messages.success(request, "Artist successfully updated.")
        return redirect('list_artists')

    # Si es GET, mostrar el formulario con los datos actuales del artista
    return render(request, 'ARTISTA/editarArtista.html', {'artist': artist})

def update_location(request, id):
    # Obtener la ubicación usando el id desde la URL
    try:
        location = Location.objects.get(id=id)
    except Location.DoesNotExist:
        messages.error(request, "Location not found.")
        return redirect('list_locations')
    
    if request.method == 'POST':
        # Actualizar los campos de la ubicación
        location.name = request.POST.get('name')
        location.address = request.POST.get('address')
        location.description = request.POST.get('description')
        
        location.save()
        messages.success(request, "Location successfully updated.")
        return redirect('list_locations')
    
    # Mostrar el formulario con los datos actuales de la ubicación
    return render(request, 'Ubicacion/editarUbicacion.html', {'location': location})

def update_organizer(request, id):
    # Obtener el organizador usando el id desde la URL
    try:
        organizer = Organizer.objects.get(id=id)
    except Organizer.DoesNotExist:
        messages.error(request, "Organizer not found.")
        return redirect('list_organizers')
    
    if request.method == 'POST':
        # Actualizar los campos del organizador
        organizer.name = request.POST.get('name')
        organizer.entity = request.POST.get('entity')
        organizer.description = request.POST.get('description')
        organizer.contact = request.POST.get('contact')
        organizer.contact_email = request.POST.get('contact_email')
        organizer.website = request.POST.get('website')
        
        organizer.save()
        messages.success(request, "Organizer successfully updated.")
        return redirect('list_organizers')
    
    # Mostrar el formulario con los datos actuales del organizador
    return render(request, 'ORGANIZADOR/editarOrganizador.html', {'organizer': organizer})


def update_event(request, id):
    # Obtener el evento usando el id desde la URL
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        messages.error(request, "Event not found.")
        return redirect('list_events')

    if request.method == 'POST':
        # Actualizar los campos del evento
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.start_date = request.POST.get('start_date')
        event.end_date = request.POST.get('end_date')
        event.status = request.POST.get('status')
        event.ARTIST_id = request.POST.get('artist')
        event.ORGANIZER_id = request.POST.get('organizer')
        event.LOCATION_id = request.POST.get('location')
        
        event.save()
        messages.success(request, "Event successfully updated.")
        return redirect('list_events')

    # Obtener los datos necesarios para los selectores en el formulario
    artists = Artist.objects.all()
    organizers = Organizer.objects.all()
    locations = Location.objects.all()

    return render(request, 'EVENTO/editarEvento.html', {'event': event, 'artists': artists, 'organizers': organizers, 'locations': locations})


def delete_artist(request, id):
    artist = get_object_or_404(Artist, id=id)
    artist.delete()
    messages.success(request, "Artist successfully deleted.")
    return redirect('list_artists')

def delete_location(request, id):
    location = get_object_or_404(Location, id=id)
    location.delete()
    messages.success(request, "Location successfully deleted.")
    return redirect('list_locations')

def delete_organizer(request, id):
    organizer = get_object_or_404(Organizer, id=id)
    organizer.delete()
    messages.success(request, "Organizer successfully deleted.")
    return redirect('list_organizers')

def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    messages.success(request, "Event successfully deleted.")
    return redirect('list_events')

def delete_event_publication(request, id):
    event_publication = get_object_or_404(EventPublication, id=id)
    event_publication.delete()
    messages.success(request, "Event publication successfully deleted.")
    return redirect('list_event_publications')

# Listar todas las licencias
def list_licenses(request):
    licenses = License.objects.all()
    return render(request, "LICENCIA/listadoLicencias.html", {'license_list': licenses})

# Crear una nueva licencia
def new_license(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        cost = request.POST.get('cost')
        initials = request.POST.get('initials')
        status = request.POST.get('status')

        license = License.objects.create(
            type=type,
            cost=cost,
            initials=initials,
            status=status
        )
        return redirect('list_licenses')
    return render(request, 'LICENCIA/nuevaLicencia.html')

# Guardar una licencia (similar a 'save_artist' para los artistas)
def save_license(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        type = request.POST.get('type')
        cost = request.POST.get('cost')
        initials = request.POST.get('initials')
        status = request.POST.get('status')
        
        # Crear la licencia
        license = License.objects.create(
            type=type,
            cost=cost,
            initials=initials,
            status=status
        )
        
        # Mensaje de éxito y redirección
        messages.success(request, "License successfully registered.")
        return redirect('list_licenses')
    
    return redirect('license_form')

# Editar una licencia
def edit_license(request, id):
    license = get_object_or_404(License, id=id)
    
    if request.method == 'POST':
        license.type = request.POST.get('type')
        license.cost = request.POST.get('cost')
        license.initials = request.POST.get('initials')
        license.status = request.POST.get('status')
        
        license.save()
        return redirect('list_licenses')
    
    return render(request, 'LICENCIA/editarLicencia.html', {'license': license})

# Actualizar una licencia
def update_license(request, id):
    # Obtener la licencia usando el id
    try:
        license = License.objects.get(id=id)
    except License.DoesNotExist:
        messages.error(request, "License not found.")
        return redirect('list_licenses')
    
    if request.method == 'POST':
        # Obtener los nuevos datos del formulario
        license.type = request.POST.get('type')
        license.cost = request.POST.get('cost')
        license.initials = request.POST.get('initials')
        license.status = request.POST.get('status')
        
        license.save()
        messages.success(request, "License successfully updated.")
        return redirect('list_licenses')

    return render(request, 'LICENCIA/editarLicencia.html', {'license': license})

# Eliminar una licencia
def delete_license(request, id):
    license = get_object_or_404(License, id=id)
    license.delete()
    messages.success(request, "License successfully deleted.")
    return redirect('list_licenses')

# Listar todas las auditorías
def list_audits(request):
    audits = Audit.objects.all()
    return render(request, "AUDITORIA/listadoAuditorias.html", {'audit_list': audits})

# Crear una nueva auditoría
def new_audit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        description = request.POST.get('description')
        user = request.POST.get('user')
        gender = request.POST.get('gender')

        audit = Audit.objects.create(
            date=date,
            description=description,
            user=user,
            gender=gender
        )
        return redirect('list_audits')
    return render(request, 'AUDITORIA/nuevaAuditoria.html')

# Guardar una auditoría (similar a 'save_artist' para los artistas)
def save_audit(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        date = request.POST.get('date')
        description = request.POST.get('description')
        user = request.POST.get('user')
        gender = request.POST.get('gender')
        
        # Crear la auditoría
        audit = Audit.objects.create(
            date=date,
            description=description,
            user=user,
            gender=gender
        )
        
        # Mensaje de éxito y redirección
        messages.success(request, "Audit successfully registered.")
        return redirect('list_audits')
    
    return redirect('audit_form')

# Editar una auditoría
def edit_audit(request, id):
    audit = get_object_or_404(Audit, id=id)
    
    if request.method == 'POST':
        audit.date = request.POST.get('date')
        audit.description = request.POST.get('description')
        audit.user = request.POST.get('user')
        audit.gender = request.POST.get('gender')
        
        audit.save()
        return redirect('list_audits')
    
    return render(request, 'AUDITORIA/editarAuditoria.html', {'audit': audit})

# Actualizar una auditoría
def update_audit(request, id):
    # Obtener la auditoría usando el id
    try:
        audit = Audit.objects.get(id=id)
    except Audit.DoesNotExist:
        messages.error(request, "Audit not found.")
        return redirect('list_audits')
    
    if request.method == 'POST':
        # Obtener los nuevos datos del formulario
        audit.date = request.POST.get('date')
        audit.description = request.POST.get('description')
        audit.user = request.POST.get('user')
        audit.gender = request.POST.get('gender')
        
        audit.save()
        messages.success(request, "Audit successfully updated.")
        return redirect('list_audits')

    return render(request, 'AUDITORIA/editarAuditoria.html', {'audit': audit})

# Eliminar una auditoría
def delete_audit(request, id):
    audit = get_object_or_404(Audit, id=id)
    audit.delete()
    messages.success(request, "Audit successfully deleted.")
    return redirect('list_audits')