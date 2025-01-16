from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    redes_sociales = models.TextField(null=True, blank=True)
    sitio_web = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Organizador(models.Model):
    nombre = models.CharField(max_length=255)
    entidad = models.CharField(max_length=255)
    descripcion = models.TextField()
    contacto = models.CharField(max_length=20, null=True, blank=True)
    email_contacto = models.EmailField(null=True, blank=True)
    sitio_web = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    ARTISTA = models.ForeignKey(Artista, on_delete=models.CASCADE)
    ORGANIZADOR = models.ForeignKey(Organizador, on_delete=models.CASCADE)
    UBICACION = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=50, choices=[('activo', 'Activo'), ('finalizado', 'Finalizado')], default='activo')

    def __str__(self):
        return self.titulo

class PublicacionEvento(models.Model):
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE, related_name="publicacion")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    hora_evento = models.TimeField()  
    contenido_publico = models.TextField()  
    imagen_evento = models.ImageField(upload_to='eventos/', null=True, blank=True)
    estado_publicacion = models.CharField(max_length=50, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    artistas_presentados = models.ManyToManyField(Artista)  
    ubicacion_evento = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Publicación de {self.evento.titulo}"

