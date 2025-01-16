from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Artista, Ubicacion, Organizador, Evento, PublicacionEvento
from .models import Artista, Ubicacion, Organizador, Evento, PublicacionEvento

def home(request):
    return render(request, 'home.html')
def home1(request):
    return render(request, 'home1.html')
# ------------------ VISTAS PARA ARTISTA ------------------
def listadoArtistas(request):
    artistas = Artista.objects.all()
    return render(request, "eventos/listado_artistas.html", {'artistas': artistas})

def nuevoArtista(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        redes_sociales = request.POST.get('redes_sociales')
        sitio_web = request.POST.get('sitio_web')

        artista = Artista(
            nombre=nombre,
            descripcion=descripcion,
            telefono=telefono,
            email=email,
            redes_sociales=redes_sociales,
            sitio_web=sitio_web
        )
        artista.save()
        messages.success(request, "Artista registrado exitosamente.")
        return redirect('listado_artistas')
    return render(request, 'eventos/nuevo_artista.html')

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
        messages.success(request, "Artista actualizado correctamente.")
        return redirect('listado_artistas')
    return render(request, 'eventos/editar_artista.html', {'artista': artista})

def eliminarArtista(request, id):
    artista = get_object_or_404(Artista, id=id)
    artista.delete()
    messages.success(request, "Artista eliminado correctamente.")
    return redirect('listado_artistas')


# ------------------ VISTAS PARA UBICACION ------------------
def listadoUbicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, "eventos/listado_ubicaciones.html", {'ubicaciones': ubicaciones})

def nuevaUbicacion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        descripcion = request.POST.get('descripcion')

        ubicacion = Ubicacion(
            nombre=nombre,
            direccion=direccion,
            descripcion=descripcion
        )
        ubicacion.save()
        messages.success(request, "Ubicación registrada exitosamente.")
        return redirect('listado_ubicaciones')
    return render(request, 'eventos/nueva_ubicacion.html')

def editarUbicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    if request.method == 'POST':
        ubicacion.nombre = request.POST.get('nombre')
        ubicacion.direccion = request.POST.get('direccion')
        ubicacion.descripcion = request.POST.get('descripcion')
        ubicacion.save()
        messages.success(request, "Ubicación actualizada correctamente.")
        return redirect('listado_ubicaciones')
    return render(request, 'eventos/editar_ubicacion.html', {'ubicacion': ubicacion})

def eliminarUbicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    ubicacion.delete()
    messages.success(request, "Ubicación eliminada correctamente.")
    return redirect('listado_ubicaciones')


# ------------------ VISTAS PARA ORGANIZADOR ------------------
def listadoOrganizadores(request):
    organizadores = Organizador.objects.all()
    return render(request, "eventos/listado_organizadores.html", {'organizadores': organizadores})

def nuevoOrganizador(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        entidad = request.POST.get('entidad')
        descripcion = request.POST.get('descripcion')
        contacto = request.POST.get('contacto')
        email_contacto = request.POST.get('email_contacto')
        sitio_web = request.POST.get('sitio_web')

        organizador = Organizador(
            nombre=nombre,
            entidad=entidad,
            descripcion=descripcion,
            contacto=contacto,
            email_contacto=email_contacto,
            sitio_web=sitio_web
        )
        organizador.save()
        messages.success(request, "Organizador registrado exitosamente.")
        return redirect('listado_organizadores')
    return render(request, 'eventos/nuevo_organizador.html')

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
        messages.success(request, "Organizador actualizado correctamente.")
        return redirect('listado_organizadores')
    return render(request, 'eventos/editar_organizador.html', {'organizador': organizador})

def eliminarOrganizador(request, id):
    organizador = get_object_or_404(Organizador, id=id)
    organizador.delete()
    messages.success(request, "Organizador eliminado correctamente.")
    return redirect('listado_organizadores')


# ------------------ VISTAS PARA EVENTO ------------------
def listadoEventos(request):
    eventos = Evento.objects.all()
    return render(request, "eventos/listado_eventos.html", {'eventos': eventos})

def nuevoEvento(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        estado = request.POST.get('estado')
        artista_id = request.POST.get('artista')
        organizador_id = request.POST.get('organizador')
        ubicacion_id = request.POST.get('ubicacion')

        artista = get_object_or_404(Artista, id=artista_id)
        organizador = get_object_or_404(Organizador, id=organizador_id)
        ubicacion = get_object_or_404(Ubicacion, id=ubicacion_id)

        evento = Evento(
            titulo=titulo,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            estado=estado,
            artista=artista,
            organizador=organizador,
            ubicacion=ubicacion
        )
        evento.save()
        messages.success(request, "Evento registrado exitosamente.")
        return redirect('listado_eventos')
    return render(request, 'eventos/nuevo_evento.html')


# ------------------ VISTAS PARA PUBLICACION DE EVENTO ------------------
def listadoPublicaciones(request):
    publicaciones = PublicacionEvento.objects.all()
    return render(request, "eventos/listado_publicaciones.html", {'publicaciones': publicaciones})

def nuevaPublicacion(request):
    if request.method == 'POST':
        evento_id = request.POST.get('evento')
        hora_evento = request.POST.get('hora_evento')
        contenido_publico = request.POST.get('contenido_publico')
        imagen_evento = request.FILES.get('imagen_evento')
        estado_publicacion = request.POST.get('estado_publicacion')

        evento = get_object_or_404(Evento, id=evento_id)

        publicacion = PublicacionEvento(
            evento=evento,
            hora_evento=hora_evento,
            contenido_publico=contenido_publico,
            imagen_evento=imagen_evento,
            estado_publicacion=estado_publicacion
        )
        publicacion.save()
        messages.success(request, "Publicación registrada exitosamente.")
        return redirect('listado_publicaciones')
    return render(request, 'eventos/nueva_publicacion.html')


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

