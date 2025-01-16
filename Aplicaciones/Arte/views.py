from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Artista, Ubicacion, Organizador, Evento, PublicacionEvento
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
def home1(request):
    return render(request, 'home1.html')

# Artista Views
def listadoArtistas(request):
    artistas = Artista.objects.all()
    return render(request, "ARTISTA/listadoArtistas.html", {'artistas': artistas})

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
    
    return render(request, 'ARTISTA/nuevoArtista.html')

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

    return render(request, 'ARTISTA/editarArtista.html', {'artista': artista})

def eliminarArtista(request, id):
    artista = Artista.objects.get(id=id)
    artista.delete()
    messages.success(request, "Artista eliminado exitosamente.")
    return redirect('listado_artistas')

# Ubicacion Views
def listadoUbicaciones(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, "UBICACION/listadoUbicacion.html", {'ubicaciones': ubicaciones})

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
    
    return render(request, 'UBICACION/nuevaUbicacion.html')

def editarUbicacion(request, id):
    ubicacion = get_object_or_404(Ubicacion, id=id)
    if request.method == 'POST':
        ubicacion.nombre = request.POST.get('nombre')
        ubicacion.direccion = request.POST.get('direccion')
        ubicacion.descripcion = request.POST.get('descripcion')
        ubicacion.save()
        messages.success(request, "Ubicación actualizada correctamente.")
        return redirect('listado_ubicaciones')

    return render(request, 'UBICACION/editarUbicacion.html', {'ubicacion': ubicacion})

def eliminarUbicacion(request, id):
    ubicacion = Ubicacion.objects.get(id=id)
    ubicacion.delete()
    messages.success(request, "Ubicación eliminada exitosamente.")
    return redirect('listado_ubicaciones')

# Organizador Views
def listadoOrganizadores(request):
    organizadores = Organizador.objects.all()
    return render(request, "ORGANIZADOR/listadoOrganizadores.html", {'organizadores': organizadores})

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
    
    return render(request, 'ORGANIZADORES/nuevoOrganizador.html')

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

    return render(request, 'ORGANIZADOR/editarOrganizador.html', {'organizador': organizador})

def eliminarOrganizador(request, id):
    organizador = Organizador.objects.get(id=id)
    organizador.delete()
    messages.success(request, "Organizador eliminado exitosamente.")
    return redirect('listado_organizadores')

# Evento Views
def listadoEventos(request):
    eventos = Evento.objects.all()
    return render(request, "EVENTO/listadoEventos.html", {'eventos': eventos})

def nuevoEvento(request):
    if request.method == 'POST':
        artista = request.POST.get('artista')
        organizador = request.POST.get('organizador')
        ubicacion = request.POST.get('ubicacion')
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        estado = request.POST.get('estado')
        
        evento = Evento(
            ARTISTA=Artista.objects.get(id=artista),
            ORGANIZADOR=Organizador.objects.get(id=organizador),
            UBICACION=Ubicacion.objects.get(id=ubicacion),
            titulo=titulo,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            estado=estado
        )
        evento.save()
        messages.success(request, "Evento registrado exitosamente.")
        return redirect('listado_eventos')
    
    return render(request, 'EVENTO/nuevoEvento.html')

def editarEvento(request, id):
    evento = get_object_or_404(Evento, id=id)
    if request.method == 'POST':
        evento.titulo = request.POST.get('titulo')
        evento.descripcion = request.POST.get('descripcion')
        evento.fecha_inicio = request.POST.get('fecha_inicio')
        evento.fecha_fin = request.POST.get('fecha_fin')
        evento.estado = request.POST.get('estado')
        evento.save()
        messages.success(request, "Evento actualizado correctamente.")
        return redirect('listado_eventos')

    return render(request, 'EVENTO/editarEvento.html', {'evento': evento})

def eliminarEvento(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    messages.success(request, "Evento eliminado exitosamente.")
    return redirect('listado_eventos')

# PublicacionEvento Views
def listadoPublicaciones(request):
    publicaciones = PublicacionEvento.objects.all()
    return render(request, "PUBLICACION/listadoPublicacion.html", {'publicaciones': publicaciones})

def nuevaPublicacion(request):
    if request.method == 'POST':
        evento = request.POST.get('evento')
        hora_evento = request.POST.get('hora_evento')
        contenido_publico = request.POST.get('contenido_publico')
        imagen_evento = request.FILES.get('imagen_evento')
        estado_publicacion = request.POST.get('estado_publicacion')
        ubicacion_evento = request.POST.get('ubicacion_evento')
        
        publicacion = PublicacionEvento(
            evento=Evento.objects.get(id=evento),
            hora_evento=hora_evento,
            contenido_publico=contenido_publico,
            imagen_evento=imagen_evento,
            estado_publicacion=estado_publicacion,
            ubicacion_evento=Ubicacion.objects.get(id=ubicacion_evento)
        )
        publicacion.save()
        messages.success(request, "Publicación de evento registrada exitosamente.")
        return redirect('listado_publicaciones')
    
    return render(request, 'PUBLICACION/nuevaPublicacion.html')

def editarPublicacion(request, id):
    publicacion = get_object_or_404(PublicacionEvento, id=id)
    if request.method == 'POST':
        publicacion.hora_evento = request.POST.get('hora_evento')
        publicacion.contenido_publico = request.POST.get('contenido_publico')
        publicacion.estado_publicacion = request.POST.get('estado_publicacion')
        publicacion.save()
        messages.success(request, "Publicación actualizada correctamente.")
        return redirect('listado_publicaciones')

    return render(request, 'PublicacionEvento/editar_publicacion.html', {'publicacion': publicacion})

def eliminarPublicacion(request, id):
    publicacion = PublicacionEvento.objects.get(id=id)
    publicacion.delete()
    messages.success(request, "Publicación eliminada exitosamente.")
    return redirect('listado_publicaciones')


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

