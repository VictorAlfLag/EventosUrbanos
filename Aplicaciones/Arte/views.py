<<<<<<< HEAD
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from Aplicaciones.Arte.forms import RegistroUsuarioForm
from .models import Artista, Ubicacion, Organizador, Evento, PublicacionEvento
from datetime import datetime
from django.contrib.auth import authenticate, login
=======
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm
from django.shortcuts import get_object_or_404
from datetime import datetime
>>>>>>> 8f99e044b8648af0827d61f17605141454ca18b1

def home(request):
    return render(request, 'home.html')
def home1(request):
    return render(request, 'home1.html')
<<<<<<< HEAD
# <----------Listado---------->
def listadoArtistas(request):
    artistas = Artista.objects.all()
    return render(request, "artistas/listadoArtistas.html", {'listado_artistas': artistas})

def listadoUbicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, "ubicaciones/listadoUbicacion.html", {'listado_ubicaciones': ubicaciones})

def listadoOrganizadores(request):
    organizadores = Organizador.objects.all()
    return render(request, "organizadores/listadoOrganizador.html", {'listado_organizadores': organizadores})

def listadoEventos(request):
    eventos = Evento.objects.all()
    return render(request, "eventos/listadoEventos.html", {'listado_eventos': eventos})

def listadoPublicacionesEventos(request):
    publicaciones = PublicacionEvento.objects.all()
    return render(request, "publicaciones/listadoPublicacion.html", {'listado_publicaciones': publicaciones})
# <--------------Nuevo------------>

def nuevoArtista(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        redes_sociales = request.POST.get('redes_sociales')
        sitio_web = request.POST.get('sitio_web')

        artista = Artista.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            telefono=telefono,
            email=email,
            redes_sociales=redes_sociales,
            sitio_web=sitio_web
        )
        return redirect('listado_artistas')
    return render(request, 'artistas/nuevoArtista.html')


def nuevaUbicacion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        descripcion = request.POST.get('descripcion')

        ubicacion = Ubicacion.objects.create(
            nombre=nombre,
            direccion=direccion,
            descripcion=descripcion
        )
        return redirect('listado_ubicaciones')
    return render(request, 'ubicaciones/nuevaUbicacion.html')


def nuevoOrganizador(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        entidad = request.POST.get('entidad')
        descripcion = request.POST.get('descripcion')
        contacto = request.POST.get('contacto')
        email_contacto = request.POST.get('email_contacto')
        sitio_web = request.POST.get('sitio_web')

        organizador = Organizador.objects.create(
            nombre=nombre,
            entidad=entidad,
            descripcion=descripcion,
            contacto=contacto,
            email_contacto=email_contacto,
            sitio_web=sitio_web
        )
        return redirect('listado_organizadores')
    return render(request, 'organizadores/nuevoOrganizador.html')


def nuevoEvento(request):
    if request.method == 'POST':
        artista = get_object_or_404(Artista, id=request.POST.get('artista'))
        organizador = get_object_or_404(Organizador, id=request.POST.get('organizador'))
        ubicacion = get_object_or_404(Ubicacion, id=request.POST.get('ubicacion'))
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        estado = request.POST.get('estado')

        evento = Evento.objects.create(
            ARTISTA=artista,
            ORGANIZADOR=organizador,
            UBICACION=ubicacion,
            titulo=titulo,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            estado=estado
        )
        return redirect('listado_eventos')
    return render(request, 'eventos/nuevoEvento.html')


def nuevaPublicacionEvento(request):
    if request.method == 'POST':
        evento = get_object_or_404(Evento, id=request.POST.get('evento'))
        hora_evento = request.POST.get('hora_evento')
        contenido_publico = request.POST.get('contenido_publico')
        imagen_evento = request.FILES.get('imagen_evento')
        estado_publicacion = request.POST.get('estado_publicacion')
        ubicacion_evento = get_object_or_404(Ubicacion, id=request.POST.get('ubicacion_evento'))

        publicacion = PublicacionEvento.objects.create(
            evento=evento,
            hora_evento=hora_evento,
            contenido_publico=contenido_publico,
            imagen_evento=imagen_evento,
            estado_publicacion=estado_publicacion,
            ubicacion_evento=ubicacion_evento
        )
        publicacion.artistas_presentados.set(request.POST.getlist('artistas_presentados'))
        return redirect('listado_publicaciones')
    return render(request, 'publicaciones/nuevaPublicacion.html')

# <--------------Guardar--------------->
def guardarArtista(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        telefono = request.POST['telefono']
        email = request.POST['email']
        redes_sociales = request.POST['redes_sociales']
        sitio_web = request.POST['sitio_web']
        
        artista = Artista.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            telefono=telefono,
            email=email,
            redes_sociales=redes_sociales,
            sitio_web=sitio_web
        )
        
        messages.success(request, "Artista registrado exitosamente.")
        return redirect('listado_artistas')
    return redirect('formulario_artista')

def guardarUbicacion(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        descripcion = request.POST['descripcion']

        Ubicacion.objects.create(
            nombre=nombre,
            direccion=direccion,
            descripcion=descripcion
        )

        messages.success(request, "Ubicación registrada exitosamente.")
        return redirect('listado_ubicaciones')
    return redirect('formulario_ubicacion')

def guardarOrganizador(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        entidad = request.POST['entidad']
        descripcion = request.POST['descripcion']
        contacto = request.POST.get('contacto', '')
        email_contacto = request.POST.get('email_contacto', '')
        sitio_web = request.POST.get('sitio_web', '')

        Organizador.objects.create(
            nombre=nombre,
            entidad=entidad,
            descripcion=descripcion,
            contacto=contacto,
            email_contacto=email_contacto,
            sitio_web=sitio_web
        )

        messages.success(request, "Organizador registrado exitosamente.")
        return redirect('listado_organizadores')
    return redirect('formulario_organizador')

def guardarEvento(request):
    if request.method == 'POST':
        artista_id = request.POST['artista']
        organizador_id = request.POST['organizador']
        ubicacion_id = request.POST['ubicacion']
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        estado = request.POST.get('estado', 'activo')

        artista = get_object_or_404(Artista, id=artista_id)
        organizador = get_object_or_404(Organizador, id=organizador_id)
        ubicacion = get_object_or_404(Ubicacion, id=ubicacion_id)

        Evento.objects.create(
            artista=artista,
            organizador=organizador,
            ubicacion=ubicacion,
            titulo=titulo,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            estado=estado
        )

        messages.success(request, "Evento registrado exitosamente.")
        return redirect('listado_eventos')
    return redirect('formulario_evento')

def guardarPublicacionEvento(request):
    if request.method == 'POST':
        evento_id = request.POST['evento']
        contenido_publico = request.POST['contenido_publico']
        hora_evento = request.POST['hora_evento']
        estado_publicacion = request.POST.get('estado_publicacion', 'activo')
        artistas_presentados_ids = request.POST.getlist('artistas_presentados')
        ubicacion_id = request.POST['ubicacion_evento']
        imagen_evento = request.FILES.get('imagen_evento', None)

        evento = get_object_or_404(Evento, id=evento_id)
        ubicacion = get_object_or_404(Ubicacion, id=ubicacion_id)

        publicacion = PublicacionEvento.objects.create(
            evento=evento,
            contenido_publico=contenido_publico,
            hora_evento=hora_evento,
            estado_publicacion=estado_publicacion,
            ubicacion_evento=ubicacion,
            imagen_evento=imagen_evento
        )

        publicacion.artistas_presentados.set(artistas_presentados_ids)

        messages.success(request, "Publicación de evento registrada exitosamente.")
        return redirect('listado_publicaciones')
    return redirect('formulario_publicacion_evento')

# <----------Editar---------->
def editarArtista(request, id):
    artista = get_object_or_404(Artista, id=id)
    
    if request.method == 'POST':
        artista.nombre = request.POST.get('nombre')
        artista.descripcion = request.POST.get('descripcion')
        artista.telefono = request.POST.get('telefono')
        artista.email = request.POST.get('email')
        artista.redes_sociales = request.POST.get('redes_sociales')
        artista.sitio_web = request.POST.get('sitio_web')
        
        artista.save()
        return redirect('listado_artistas')
    
    return render(request, 'artistas/editarArtista.html', {'artista': artista})

def editarUbicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    if request.method == 'POST':
        ubicacion.nombre = request.POST.get('nombre')
        ubicacion.direccion = request.POST.get('direccion')
        ubicacion.descripcion = request.POST.get('descripcion')
        ubicacion.save()
        return redirect('listado_ubicaciones')
    return render(request, 'ubicaciones/editarUbicacion.html', {'ubicacion': ubicacion})

def editarOrganizador(request, id):
    organizador = get_object_or_404(Organizador, id=id)
    if request.method == 'POST':
        organizador.nombre = request.POST.get('nombre')
        organizador.entidad = request.POST.get('entidad')
        organizador.descripcion = request.POST.get('descripcion')
        organizador.contacto = request.POST.get('contacto')
        organizador.email_contacto = request.POST.get('email_contacto')
        organizador.sitio_web = request.POST.get('sitio_web')
        organizador.save()
        return redirect('listado_organizadores')
    return render(request, 'organizadores/editarOrganizador.html', {'organizador': organizador})

def editarEvento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.titulo = request.POST.get('titulo')
        evento.descripcion = request.POST.get('descripcion')
        evento.fecha_inicio = request.POST.get('fecha_inicio')
        evento.fecha_fin = request.POST.get('fecha_fin')
        evento.estado = request.POST.get('estado')
        evento.ARTISTA_id = request.POST.get('artista')
        evento.ORGANIZADOR_id = request.POST.get('organizador')
        evento.UBICACION_id = request.POST.get('ubicacion')
        evento.save()
        return redirect('listado_eventos')
    artistas = Artista.objects.all()
    organizadores = Organizador.objects.all()
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'eventos/editarEvento.html', {'evento': evento, 'artistas': artistas, 'organizadores': organizadores, 'ubicaciones': ubicaciones})

def editarPublicacionEvento(request, id):
    publicacion = get_object_or_404(PublicacionEvento, id=id)
    if request.method == 'POST':
        publicacion.contenido_publico = request.POST.get('contenido_publico')
        publicacion.estado_publicacion = request.POST.get('estado_publicacion')
        publicacion.hora_evento = request.POST.get('hora_evento')
        publicacion.imagen_evento = request.FILES.get('imagen_evento') if 'imagen_evento' in request.FILES else publicacion.imagen_evento
        publicacion.evento_id = request.POST.get('evento')
        publicacion.ubicacion_evento_id = request.POST.get('ubicacion_evento')
        publicacion.save()
        artistas = request.POST.getlist('artistas_presentados')
        publicacion.artistas_presentados.set(artistas)
        return redirect('listado_publicaciones')
    eventos = Evento.objects.all()
    ubicaciones = Ubicacion.objects.all()
    artistas = Artista.objects.all()
    return render(request, 'publicaciones/editarPublicacion.html', {'publicacion': publicacion, 'eventos': eventos, 'ubicaciones': ubicaciones, 'artistas': artistas})

# <-------------Actualizar-------->
def procesoActualizarArtista(request):
    id_artista = request.POST.get('id')
    if not id_artista:
        messages.error(request, "El ID del artista no fue enviado correctamente.")
        return redirect('listado_artistas')
    
    nombre = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    telefono = request.POST.get('telefono')
    email = request.POST.get('email')
    redes_sociales = request.POST.get('redes_sociales')
    sitio_web = request.POST.get('sitio_web')
    
    try:
        artista = Artista.objects.get(id=id_artista)
    except Artista.DoesNotExist:
        messages.error(request, "Artista no encontrado.")
        return redirect('listado_artistas')
    
    artista.nombre = nombre
    artista.descripcion = descripcion
    artista.telefono = telefono
    artista.email = email
    artista.redes_sociales = redes_sociales
    artista.sitio_web = sitio_web
    artista.save()
    
    messages.success(request, "Artista actualizado correctamente.")
    return redirect('listado_artistas')

def procesoActualizarUbicacion(request):
    id_ubicacion = request.POST.get('id')
    if not id_ubicacion:
        messages.error(request, "El ID de la ubicación no fue enviado correctamente.")
        return redirect('listado_ubicaciones')

    nombre = request.POST.get('nombre')
    direccion = request.POST.get('direccion')
    descripcion = request.POST.get('descripcion')

    try:
        ubicacion = Ubicacion.objects.get(id=id_ubicacion)
    except Ubicacion.DoesNotExist:
        messages.error(request, "Ubicación no encontrada.")
        return redirect('listado_ubicaciones')

    ubicacion.nombre = nombre
    ubicacion.direccion = direccion
    ubicacion.descripcion = descripcion
    ubicacion.save()

    messages.success(request, "Ubicación actualizada correctamente.")
    return redirect('listado_ubicaciones')

def procesoActualizarOrganizador(request):
    id_organizador = request.POST.get('id')
    if not id_organizador:
        messages.error(request, "El ID del organizador no fue enviado correctamente.")
        return redirect('listado_organizadores')

    nombre = request.POST.get('nombre')
    entidad = request.POST.get('entidad')
    descripcion = request.POST.get('descripcion')
    contacto = request.POST.get('contacto')
    email_contacto = request.POST.get('email_contacto')
    sitio_web = request.POST.get('sitio_web')

    try:
        organizador = Organizador.objects.get(id=id_organizador)
    except Organizador.DoesNotExist:
        messages.error(request, "Organizador no encontrado.")
        return redirect('listado_organizadores')

    organizador.nombre = nombre
    organizador.entidad = entidad
    organizador.descripcion = descripcion
    organizador.contacto = contacto
    organizador.email_contacto = email_contacto
    organizador.sitio_web = sitio_web
    organizador.save()

    messages.success(request, "Organizador actualizado correctamente.")
    return redirect('listado_organizadores')

def procesoActualizarEvento(request):
    id_evento = request.POST.get('id')
    if not id_evento:
        messages.error(request, "El ID del evento no fue enviado correctamente.")
        return redirect('listado_eventos')

    titulo = request.POST.get('titulo')
    descripcion = request.POST.get('descripcion')
    fecha_inicio = request.POST.get('fecha_inicio')
    fecha_fin = request.POST.get('fecha_fin')
    estado = request.POST.get('estado')

    try:
        evento = Evento.objects.get(id=id_evento)
    except Evento.DoesNotExist:
        messages.error(request, "Evento no encontrado.")
        return redirect('listado_eventos')

    evento.titulo = titulo
    evento.descripcion = descripcion
    evento.fecha_inicio = fecha_inicio
    evento.fecha_fin = fecha_fin
    evento.estado = estado
    evento.save()

    messages.success(request, "Evento actualizado correctamente.")
    return redirect('listado_eventos')


def procesoActualizarPublicacionEvento(request):
    id_publicacion = request.POST.get('id')
    if not id_publicacion:
        messages.error(request, "El ID de la publicación no fue enviado correctamente.")
        return redirect('listado_publicaciones_eventos')

    contenido_publico = request.POST.get('contenido_publico')
    estado_publicacion = request.POST.get('estado_publicacion')

    try:
        publicacion = PublicacionEvento.objects.get(id=id_publicacion)
    except PublicacionEvento.DoesNotExist:
        messages.error(request, "Publicación no encontrada.")
        return redirect('listado_publicaciones_eventos')

    publicacion.contenido_publico = contenido_publico
    publicacion.estado_publicacion = estado_publicacion
    publicacion.save()
    messages.success(request, "Publicación actualizada correctamente.")
    return redirect('listado_publicaciones_eventos')

# <-------------Eliminar-------->
def eliminarArtista(request, id):
    artista = get_object_or_404(Artista, id=id)
    artista.delete()
    messages.success(request, "Artista eliminado exitosamente.")
    return redirect('listado_artistas')

def eliminarUbicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    ubicacion.delete()
    messages.success(request, "Ubicación eliminada exitosamente.")
    return redirect('listado_ubicaciones')

def eliminarOrganizador(request, id):
    organizador = get_object_or_404(Organizador, id=id)
    organizador.delete()
    messages.success(request, "Organizador eliminado exitosamente.")
    return redirect('listado_organizadores')

def eliminarEvento(request, id):
    evento = get_object_or_404(Evento, id=id)
    evento.delete()
    messages.success(request, "Evento eliminado exitosamente.")
    return redirect('listado_eventos')

def eliminarPublicacionEvento(request, id):
    publicacion_evento = get_object_or_404(PublicacionEvento, id=id)
    publicacion_evento.delete()
    messages.success(request, "Publicación de evento eliminada exitosamente.")
    return redirect('listado_publicaciones')
# <-------------Login-------->
=======

>>>>>>> 8f99e044b8648af0827d61f17605141454ca18b1
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "¡Usuario creado exitosamente!")
            return redirect('home1') 
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
            return render(request, 'Login/registro.html', {'form': form})
    else:
        form = RegistroUsuarioForm()
    return render(request, 'Login/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        print(request.POST)  
        if 'usuario' in request.POST and 'clave' in request.POST:
            username = request.POST['usuario']
            password = request.POST['clave']
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home1')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Campos de usuario o contraseña faltantes.')
    return render(request, 'login/login.html')

