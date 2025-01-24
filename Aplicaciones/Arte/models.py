from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    social_media = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Artist'

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Location'

class Organizer(models.Model):
    name = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)
    description = models.TextField()
    contact = models.CharField(max_length=20, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Organizer'

class Event(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE) 
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE) 
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('finished', 'Finished')], default='active')

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Event'

class EventPublication(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name="publication")
    publication_date = models.DateTimeField(auto_now_add=True)
    event_time = models.TimeField()  
    public_content = models.TextField()  
    event_image = models.ImageField(upload_to='events/', null=True, blank=True)
    publication_status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    featured_artists = models.ManyToManyField(Artist)  
    event_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"Publication of {self.event.title}"
    class Meta:
        db_table = 'ventPublication'

class License(models.Model):
    TYPE_CHOICES = [
        ('professional', 'Professional'),
        ('normal', 'Normal'),
        # Puedes agregar más tipos si es necesario
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('expired', 'Expired'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)  
    cost = models.DecimalField(max_digits=10, decimal_places=2) 
    initials = models.CharField(max_length=50) 
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)  
    
    def __str__(self):
        return f"License {self.id} - {self.type}"

    class Meta:
        db_table = 'License'  
        
class Audit(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    date = models.DateTimeField()  
    description = models.TextField() 
    user = models.CharField(max_length=255) 
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)  
    def __str__(self):
        return f"Audit {self.id}"

    class Meta:
        db_table = 'Audit'
